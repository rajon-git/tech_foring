
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from userauths.views import RegisterView, LoginView, LogoutView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API",
        default_version='v1',
        description="API documentation for the Project Management app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', include('project_management.urls')),
    path('api/', include('tasks.urls')),
    path('api/users/', include('userauths.urls')),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    
    # Documenttaion
    path('', schema_view.with_ui('swagger', cache_timeout = 0), name="schema-swagger-ui"),
]

