
from django.contrib.auth.models import PermissionsMixin
from django.db import models# Create your models here.
""" import django
django.setup() """
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class MyUserManager(BaseUserManager):
    def create_superuser(self, email, username, password):
        user = self.model( 
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class ImdbUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_staff = models.BooleanField(
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label=True):
        return True

@receiver(post_save, sender=ImdbUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)