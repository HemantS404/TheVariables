from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CORE API",
        default_version='v1',
        description="Built by Hemant Singh",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('',schema_view.with_ui(cache_timeout=0), name='schema-json'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('company_handle/', include('compony_handle.urls')),
    path('job_handle/', include('job_handle.urls')),
    path('model/', include('deploy_model.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)