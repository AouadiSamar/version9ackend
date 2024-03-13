from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Assuming CustomUserManager is correctly defined in managers.py
class Role(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)
    description = models.TextField(_("Description"), blank=True)
    permissions = models.ManyToManyField('Permission', related_name='roles')

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)
    description = models.TextField(_("Description"), blank=True)

    def __str__(self):
        return self.name

# Define User here





from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email Address"), unique=True)
    phone_number = models.CharField(_("Phone Number"), max_length=20, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    # New fields
    phone = models.CharField(max_length=20, blank=True, null=True)  # This field seems to duplicate 'phone_number'
    creation_date = models.DateTimeField(auto_now_add=False, default=now)
    expiration_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True, default='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

# Now it's safe to define UserRole and RolePermission
class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.user.email} - {','.join([role.name for role in self.roles.all()])}"

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return f"{self.role.name} - {','.join([permission.name for permission in self.permissions.all()])}"






from django.db import models
from django.contrib.auth import get_user_model



from django.conf import settings
from django.db import models
from django.db import models
from django.conf import settings

class UserActivity(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.activity} - {self.timestamp}"




