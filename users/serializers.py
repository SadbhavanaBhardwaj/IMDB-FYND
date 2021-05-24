from users.models import ImdbUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    pswd2 = serializers.CharField(write_only=True)

    class Meta:
        model = ImdbUser
        fields = ['email', 'password', 'pswd2', 'first_name', 'last_name', 'username']


    def save(self):
        data = self.validated_data
        user = ImdbUser(email=data['email'], 
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['username'])
        if data['password'] != data['pswd2']:
            raise serializers.ValidationError({"msg": "Both passwords should be same."})
        user.set_password(data['password'])
        user.save()
        return user