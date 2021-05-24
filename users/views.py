from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from users.models import ImdbUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users.serializers import UserSerializer


import json

class CreateUser(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        return_data = {}
        if serializer.is_valid():
            user = serializer.save()
            return_data['response'] = "Successfully regisered the user"
            return_data['email'] = user.email
            return_data['token'] = Token.objects.get(user=user).key
            if 'group' in data:
                group = Group.objects.get(name=data['group'])
                user.groups.add(group.id)
        else:
            return_data = serializer.errors
        return Response(return_data)            
