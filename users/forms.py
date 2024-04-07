from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Role, User, UserRole  # Assuming your User model is here
# users/forms.py
from django import forms


# Your form classes here...

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = User
    fields = ["email", "first_name", "last_name"]
    error_classes = {'username': 'invalid-username'}  # Example custom error class

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = User
    fields = ["email", "first_name", "last_name"]
    error_classes = {'email': 'invalid-email'}  # Example custom error class

# Your custom forms for roles and permissions (replace with your models)
class UserRoleForm(forms.ModelForm):
  class Meta:
    model = UserRole
    fields = ['user', 'roles']
    widgets = {
      'roles': forms.CheckboxSelectMultiple(),
    }

class RolePermissionForm(forms.ModelForm):
  class Meta:
    model = Role
    fields = ['permissions']
    widgets = {
      'permissions': forms.CheckboxSelectMultiple(),
    }
