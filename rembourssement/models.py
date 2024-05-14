from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Rembourssement(models.Model):
    is_active = models.BooleanField(default=True, help_text="Indicates whether the rembourssement is active or not.")


    title = models.CharField(max_length=100)
    description = models.TextField()
    authorization_number = models.CharField(_("Authorization Number"), max_length=255,null=True,  blank=False,unique=True)
    amount = models.DecimalField(_("Amount"), max_digits=10, unique=True, null=True,decimal_places=2)
    merchant_number = models.CharField(_("Merchant Number"), null=True,max_length=255)
    merchant_email = models.EmailField(_("Merchant Email"),unique=True,null=True)
    merchant_name = models.CharField(_("Merchant Name"), null=True,max_length=255)

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_rembourssements',
        verbose_name=_("Assigned To")
    )

    STATUS_CHOICES = [
        ('created', _('Created')),
        ('sent_to_merchant', _('Sent to Merchant')),
        ('processing_by_SMT', _('Processing by SMT')),
        ('processing_by_bank', _('Processing by Bank')),
        ('won', _('Won')),
        ('lost', _('Lost')),
        ('cancelled', _('Cancelled')),
        ('reactivate', _('Reactivate')),


    ]

    status = models.CharField(_("Status"), max_length=100, choices=STATUS_CHOICES, null=True)
    reason = models.TextField(_("Reason"),null=True)
    creation_date = models.DateTimeField(_("Creation Date"), default=timezone.now)
    modification_date = models.DateTimeField(_("Modification Date"), auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE, related_name='created_rembourssements')

    class Meta:
        verbose_name = _("Rembourssement")
        verbose_name_plural = _("Rembourssement")

    def __str__(self):
        return f"Rembourssement{self.title} - {self.authorization_number} - {self.status}"
    
    
 

from django.db import models




from django.db import models
from django.conf import settings

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rembourssement= models.ForeignKey(Rembourssement, related_name='commentss', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE, related_name='commentss')

    def __str__(self):
        return self.text[:50]



    

from django.db import models
from django.conf import settings

from django.db import models
from django.conf import settings

# models.py
from django.db import models
from django.conf import settings

class ActionLog(models.Model):
    rembourssement = models.ForeignKey('Rembourssement', related_name='log', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='action_log')

    def __str__(self):
        return f'{self.created_at.strftime("%Y-%m-%d %H:%M:%S")} - {self.action} by {self.user.email}'



from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    rembourssement = models.ForeignKey(Rembourssement, related_name='files', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
