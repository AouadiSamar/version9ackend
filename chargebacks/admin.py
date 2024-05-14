
# admin.py
from django.contrib import admin

from .models import ActionLog , Comment
from .models import Chargeback

class ActionLogAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'action', 'user', 'chargeback']
    search_fields = ['action', 'user__email', 'chargeback__title']
    list_filter = ['created_at', 'user']
    readonly_fields = ['created_at', 'user', 'action', 'chargeback']










class ChargebackAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def delete_model(self, request, obj):
        obj.created_by = request.user  
        obj.delete()

admin.site.register(Chargeback, ChargebackAdmin)





admin.site.register(ActionLog,ActionLogAdmin)
