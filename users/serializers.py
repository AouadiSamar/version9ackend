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


from rest_framework import serializers
from .models import User, Role

from rest_framework import serializers

from .models import Role, Permission

from rest_framework import serializers
from .models import Role, Permission

class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(many=True, queryset=Permission.objects.all())

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'permissions']


    def create(self, validated_data):
        permissions = validated_data.pop('permissions')
        role = Role.objects.create(**validated_data)
        role.permissions.set(permissions)  # Assign permissions to the role
        return role

    def update(self, instance, validated_data):
        permissions = validated_data.pop('permissions', [])  # Handle optional 'permissions'
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.permissions.set(permissions)  # Update permissions
        instance.save()
        return instance
from rest_framework import serializers
from .models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'




from rest_framework import serializers
from .models import User, Role


from rest_framework import serializers
from .models import User, Role
from rest_framework import serializers
from .models import User, Role

from rest_framework import permissions 


class UserSerializer(serializers.ModelSerializer):
    role_names = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'is_staff', 'is_active', 'creation_date', 'expiration_date', 'status', 'roles', 'role_names']
        permissions_classes = [permissions.IsAuthenticated]

    def get_role_names(self, obj):
        return [role.name for role in obj.roles.all()]
    

    def create(self, validated_data):
        roles_data = validated_data.pop('roles', [])
        user = User.objects.create(**validated_data)
        user.roles.set(roles_data)
        return user
    
    def update(self, instance, validated_data):
        roles_data = validated_data.pop('roles', None)
        print("oo")
        if roles_data is not None:
            print("aa")
            instance.roles.set(roles_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    




    # serializers.py
# serializers.py
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()



