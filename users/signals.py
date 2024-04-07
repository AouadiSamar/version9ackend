from django.contrib.sessions.models import Session
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

INACTIVITY_TIMEOUT = timedelta(minutes=30)  # Adjust this to your desired timeout

@receiver(user_logged_in)
def update_session_last_activity(sender, user, request, **kwargs):
    session_key = request.session.session_key
    try:
        session = Session.objects.get(session_key=session_key)
        # Update the session's expiry time.
        session.expire_date = timezone.now() + INACTIVITY_TIMEOUT
        session.save()
    except Session.DoesNotExist:
        # Handle case where session does not exist if necessary.
        pass

@receiver(user_logged_in, dispatch_uid="expire_old_sessions")
def expire_old_sessions(sender, user, request, **kwargs):
    current_session_key = request.session.session_key
    # Filter sessions based on expiry and custom logic.
    for session in Session.objects.filter(expire_date__gte=timezone.now()):
        session_data = session.get_decoded()
        last_activity = session_data.get('last_activity')
        if last_activity is None or (timezone.now() - last_activity > INACTIVITY_TIMEOUT):
            if session.session_key != current_session_key:
                session.delete()

















# signals.py or views.py within your Django app


