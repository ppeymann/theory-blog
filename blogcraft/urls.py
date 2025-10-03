from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog Craft",
        default_version='v1',
        description="API Documentation for Blog Craft",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="p.malek32@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('user/', include('user.urls')),
    path('swagger/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
