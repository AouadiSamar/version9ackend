
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Rembourssement, ActionLog
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=Rembourssement)
def log_rembourssement_save(sender, instance, created, **kwargs):
    action = "Created" if created else "Updated"
    ActionLog.objects.create(
        rembourssement=instance,
        action=action,
        user=instance.created_by if hasattr(instance, 'created_by') else None
    )

from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Rembourssement

@receiver(post_save, sender=Rembourssement)
def send_notification_on_change(sender, instance, created, **kwargs):
    if created:
        subject = f'New Rembourssement Created: ID {instance.id}'
        message = f'A new rembourssement with ID {instance.id} has been created.'
    else:
        subject = f'Rembourssement Updated: ID {instance.id}'
        message = f'The rembourssement with ID {instance.id} has been updated.'
    
    send_notification_email(subject, message)



def send_notification_email(subject, message):
    User = get_user_model()
    superadmins = User.objects.filter(is_superuser=True).values_list('email', flat=True)
    send_mail(
        subject,
        message,
        'samaraouadi7@gmail.com',  # Your from email address
        superadmins,
        fail_silently=False,
    )
