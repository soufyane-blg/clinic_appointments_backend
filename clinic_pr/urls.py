"""
URL configuration for clinic_pr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


# API Root
@api_view(["GET"])
def api_root(request):
    return Response({
        "accounts": "/api/accounts/",
        "appointments": "/api/appointments/",
        "doctors": "/api/doctors/",
        "organizations": "/api/organizations/",
        "schedules": "/api/schedules/",
        "token": "/api/token/",
        "token_refresh": "/api/token/refresh/",
    })


urlpatterns = [

    # Admin
    path("admin/", admin.site.urls),

    # API Root
    path("api/", api_root, name="api-root"),

    # JWT Authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Apps APIs
    path("api/accounts/", include("accounts.urls")),
    path("api/appointments/", include("appointments.urls")),
    path("api/doctors/", include("doctors.urls")),
    path("api/organizations/", include("organizations.urls")),
    path("api/schedules/", include("schedules.urls")),

    # API Schema and Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]