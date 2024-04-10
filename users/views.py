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

from django.contrib.messages import success


# Import your custom forms (assuming they are in the same directory)

from django.contrib.sessions.models import Session
from django.utils import timezone
from django.shortcuts import render

from django.http import JsonResponse
from django.utils import timezone

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
from django.contrib.sessions.models import Session

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
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role  # Ajustez l'import selon votre modèle de rôle

class ProfileView(serializers.ModelSerializer):
    role_names = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'address', 'role_names']  # Ajustez selon vos champs

    def get_role_names(self, obj):
        return [role.name for role in obj.roles.all()]  # Assurez-vous que 'roles' est le nom de la relation dans votre modèle User





from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from rest_framework import status


        # La suite de votre logique...





from django.contrib.auth.models import User






















from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import User  # Importation correcte du modèle utilisateur personnalisé
from users.serializers import RoleSerializer, UserSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import User  # Assurez-vous d'importer votre modèle User
from .serializers import UserSerializer  # Assurez-vous d'importer le bon serializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        try:
            # L'utilisateur est déjà authentifié et son instance est disponible via `request.user`
            user = request.user
            if not user:
                raise AuthenticationFailed('Utilisateur non trouvé')
                
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

class UserUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # If needed, override the update method or perform any additional logic here



    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(data=request.data, instance=self.get_object(), partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(serializer.instance, '_prefetched_objects_cache', None):
            # we need to invalidate the prefetch cache on the instance.
            serializer.instance._prefetched_objects_cache = {}

        return Response(serializer.data)


from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer  # Assurez-vous que le chemin d'importation est correct
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
class UserCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # La méthode save appelle create dans le serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    # permission_classes = [permissions.IsAuthenticated] # Assurez-vous que ceci est approprié pour votre cas d'usage


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
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
    permission_classes = [IsAuthenticated]

    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_serializer_context(self):
        """
        Ajoute des informations contextuelles au sérialiseur pour inclure les utilisateurs ayant le rôle.
        """
        context = super().get_serializer_context()
        context['users'] = self.get_object().users.all()
        return context



from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAuthenticated

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from rest_framework.exceptions import PermissionDenied



from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }










from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views import View



from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from users.models import User  # Make sure this points to your User model

class SendResetEmailView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"http://localhost:5173/reset-password-form/{uid}/{token}"

            subject = "Reset Your Password :Paymee"
            message = f"You're receiving this email because you requested a password reset for your user account at Paymee.Please go to the following page and choose a new password:{reset_link}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                return Response({"message": "Reset password email sent successfully."}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": f"Failed to send email. Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)














