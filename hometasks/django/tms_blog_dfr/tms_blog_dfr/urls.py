from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import RegisterView, UserMeView

schema_view = get_schema_view(
    openapi.Info(
        title="Django Restfull Blog-TMS",
        default_version='v1',
        description="main api",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@site.local"),
        license=openapi.License(name="license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'posts', PostViewSet)
# router.register(r'commets', CommentsViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('test/me/', UserMeView.as_view(), name='user-me'),
    path('auth/sign-up/', RegisterView.as_view(), name='sign-up'),
    path('auth/sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     ------------
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
