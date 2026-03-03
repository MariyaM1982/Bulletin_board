from django.contrib import admin
from django.urls import path, include
from django_rest_passwordreset.views import ResetPasswordRequestToken, ResetPasswordConfirm
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Доска объявлений API",
        default_version='v1',
        description="API для сайта объявлений",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # Добавляем Bearer Auth
    authentication_classes=(),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/reset_password/', ResetPasswordRequestToken.as_view(), name='reset-password-request'),
    path('api/users/reset_password_confirm/', ResetPasswordConfirm.as_view(), name='reset-password-confirm'),
    path('api/', include('ads.urls')),
    path('api/auth/', include('users.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]