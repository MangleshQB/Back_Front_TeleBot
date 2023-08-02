from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view
from Custom_User.views import *
from Categories.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="E-Commerce API",
      default_version='v1',
      description="API for E-Commerce Telegram Bot",
      terms_of_service="",
      contact=openapi.Contact(email="info@quantumbot.in"),
      license=openapi.License(name="QB E-Commerce Bot"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', Product),
    path('favicon/', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('productlist/', ProductViewSet.as_view({'get': 'list'})),
    path('categorylist/', CategoryViewSet.as_view({'get': 'list'})),
    path('login/', Login),
    path('signup/', RegistrationView.as_view({'get': 'list', 'post': 'create'})),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),   name='schema-swagger-ui'),
]
