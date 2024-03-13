from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer


User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'address']  # Adjust fields as needed





from django.contrib.auth.models import User
from rest_framework import serializers


class ActivateDeactivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_active']


def activate_user(user_id):
    serializer = ActivateDeactivateUserSerializer(data={'is_active': True})
    if serializer.is_valid():
        serializer.save(pk=user_id)  # Update existing user

def deactivate_user(user_id):
    serializer = ActivateDeactivateUserSerializer(data={'is_active': False})
    if serializer.is_valid():
        serializer.save(pk=user_id)

        



from .models import User  # Assuming your User model is here

from rest_framework import serializers
from django.contrib.auth import get_user_model  # Use this to get the user model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Adjust fields based on your User model
