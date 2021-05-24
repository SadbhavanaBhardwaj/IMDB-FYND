
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from users.views import CreateUser

urlpatterns = [
    path('register/', CreateUser.as_view()),
    path('login/', views.obtain_auth_token)
]
