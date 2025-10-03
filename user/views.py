from django.contrib.auth.models import User
from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


# Create your views here.

class CreateUserView(generics.CreateAPIView):
    # Public user registration
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class AccountView(APIView):
    # Return current authenticated user info
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })

class UserListView(generics.ListAPIView):
    # List all users (admin only)
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self) -> QuerySet:
        return User.objects.all()