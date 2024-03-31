from rest_framework import status, views
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated

class UserView(views.APIView):

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
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import User  # Importation correcte du modèle utilisateur personnalisé
from users.serializers import RoleSerializer, UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['put']  # Only allow PUT requests

def put(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_object(), data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']  # Only allow GET requests

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework import generics
from .models import User
from .serializers import UserSerializer
# Django view for updating a user
from rest_framework import generics
from .serializers import UserSerializer

from rest_framework.generics import UpdateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer  # Adjust the import path as needed
from .models import User  # Adjust the import path as needed

from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer  # Adjust the import path as needed
from .models import User  # Adjust the import path as needed
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User



from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework import status, generics
from rest_framework.response import Response
from .models import User

from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated  # Optionnel, pour la sécurité
from .models import User
from .serializers import UserSerializer  # Ajustez selon votre cas


from rest_framework.generics import DestroyAPIView
from .models import User
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

class UserDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User

class ToggleUserActiveStatus(APIView):
    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.is_active = not user.is_active
        user.save()
        return Response({"success": True, "is_active": user.is_active}, status=status.HTTP_200_OK)



from rest_framework import generics, permissions
from .models import Role
from .serializers import RoleSerializer




from rest_framework import generics
from .models import Role
from .serializers import RoleSerializer
# from rest_framework import permissions

class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
# In your Django app's views.py
from rest_framework.generics import ListAPIView


from .models import Role
from rest_framework import generics, permissions, status
from rest_framework.response import Response

class RoleUpdateView(generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(data=request.data, instance=self.get_object(), partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(serializer.instance, '_prefetched_objects_cache', None):
            # we need to invalidate the prefetch cache on the instance.
            serializer.instance._prefetched_objects_cache = {}

        return Response(serializer.data)

from .models import Role
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Role, Permission
from .serializers import RoleSerializer

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Role, Permission  # Assuming models are defined elsewhere
from .serializers import RoleSerializer

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Role, Permission
from .serializers import RoleSerializer
from django.shortcuts import render
from .models import Permission  # Import your Permission model

from rest_framework.generics import ListAPIView
from .models import Permission
from .serializers import PermissionSerializer

class PermissionListView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class RoleCreateView(APIView):

    def post(self, request, format=None):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .models import Role
from rest_framework import generics, permissions, serializers

class RoleDetailView(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_serializer_context(self):
        """
        Ajoute des informations contextuelles au sérialiseur pour inclure les utilisateurs ayant le rôle.
        """
        context = super().get_serializer_context()
        context['users'] = self.get_object().users.all()
        return context

