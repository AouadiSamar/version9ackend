from django.contrib import admin

# Register your models here.
from django.contrib import admin
# admin.py
from django.contrib import admin
from .models import ActionLog

class ActionLogAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'action', 'user', 'rembourssement']
    search_fields = ['action', 'user__email', 'chargeback__title']
    list_filter = ['created_at', 'user']
    readonly_fields = ['created_at', 'user', 'action', 'rembourssement']

admin.site.register(ActionLog, ActionLogAdmin)


# admin.py
from django.contrib import admin
from .models import Rembourssement

class ChargebackAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def delete_model(self, request, obj):
        obj.created_by = request.user  # Ensure the user is set before deletion
        obj.delete()

admin.site.register(Rembourssement, ChargebackAdmin)
