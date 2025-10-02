from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CreateUserView, AccountView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('', include('rest_framework.urls')),
    path('', AccountView.as_view(), name='account'),


]