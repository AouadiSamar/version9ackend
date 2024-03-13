from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Role, Permission, UserRole
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ActivateDeactivateUserSerializer  # Import the serializer

# UserAdmin configuration with custom actions for activation/deactivation
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Role, Permission, UserRole
from .forms import CustomUserChangeForm, CustomUserCreationForm

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Register the User model with the custom UserAdmin
admin.site.register(User, UserAdmin)



# Admin configurations for other models (Role, Permission, UserRole)

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    filter_horizontal = ('permissions',)

class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'list_roles']
    search_fields = ['user__email']
    filter_horizontal = ('roles',)

    def list_roles(self, obj):
        return ", ".join([role.name for role in obj.roles.all()])

    list_roles.short_description = _("Roles")


# Register admin models
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserRole)




# N'oubliez pas d'enregistrer votre modèle User avec la classe UserAdmin personnalisée


































