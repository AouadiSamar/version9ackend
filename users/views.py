from rest_framework import status, views
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated

class UserView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.decorators import login_required
from django.contrib.messages import success


# Import your custom forms (assuming they are in the same directory)

from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.utils import timezone

@login_required
def active_sessions(request):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    active_sessions = []
    for session in sessions:
        session_data = session.get_decoded()
        if session_data.get('_auth_user_id') == str(request.user.id):
            active_sessions.append({
                'session_key': session.session_key,
                'expire_date': session.expire_date,
            })
    
    return JsonResponse({'active_sessions': active_sessions})


from django.shortcuts import redirect

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session

@login_required
def terminate_session(request, session_key):
    response = {'status': 'failed', 'message': 'Session not found.'}
    if request.method == 'POST':  # Assurez-vous que la requête est une requête POST
        try:
            session = Session.objects.get(session_key=session_key)
            if session.get_decoded().get('_auth_user_id') == str(request.user.id):
                session.delete()
                response = {'status': 'success', 'message': 'Session terminated successfully.'}
            else:
                response = {'status': 'failed', 'message': 'Permission denied.'}
        except Session.DoesNotExist:
            pass
    else:
        response = {'status': 'failed', 'message': 'Invalid request method.'}
    
    return JsonResponse(response)


from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer  # Import the serializer

# ... rest of your view code
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer  # Import the serializer you created for the User model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer  # Adjust import as needed

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer  # Assuming your serializer is in a file named serializers.py
class ProfileView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

  def post(self, request):
    serializer = UserSerializer(request.user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
