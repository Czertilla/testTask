from .views import index
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi

router = DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Libabook API",
      default_version="v1"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('home/', index),
]