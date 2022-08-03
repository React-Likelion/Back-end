from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


#스웨거 적용 내용
schema_view = get_schema_view(
    openapi.Info(
        title="Re:act",
        default_version='v1',
        description="은퇴 후 제 2의 삶을 위한 플랫폼", 
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kathyleesh7@gmail.com"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

]
