from django.contrib import admin
from .models import * 

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Role, Permission, UserRole, RolePermission, UserActivity
# users/admin.py


# Your admin registration here...

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'address', 'expiration_date', 'status')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),  # 'date_joined' n'est pas nécessaire car généralement géré automatiquement par Django
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

# Admin for Role
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Admin for Permission
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Admin for UserRole
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'get_roles')
    search_fields = ('user__email',)

    def user_email(self, obj):
        return obj.user.email

    def get_roles(self, obj):
        return ", ".join([role.name for role in obj.roles.all()])

# Admin for RolePermission
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'get_permissions')
    search_fields = ('role__name',)

    def role_name(self, obj):
        return obj.role.name

    def get_permissions(self, obj):
        return ", ".join([permission.name for permission in obj.permissions.all()])

# Admin for UserActivity
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'activity', 'timestamp')
    search_fields = ('user__email', 'activity')

    def user_email(self, obj):
        return obj.user.email

# Registering models with their respective admins
admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(RolePermission, RolePermissionAdmin)
admin.site.register(UserActivity, UserActivityAdmin)
