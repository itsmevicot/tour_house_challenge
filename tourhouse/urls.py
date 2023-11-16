"""
URL configuration for tourhouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from rest_framework import permissions
from tourhouse import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Tour House API",
      default_version='v1',
      description="API's to the Tour House project.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),

    path('api/v1/', include('authentication.urls', namespace='authentication')),
    path('api/v1/', include('apis.employees.urls', namespace='employees')),
    path('api/v1/', include('apis.companies.urls', namespace='companies')),
    path('api/v1/', include('apis.departments.urls', namespace='departments')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
