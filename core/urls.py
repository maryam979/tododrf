from rest_framework.routers import DefaultRouter
from django.urls import path, include

from core import views

router = DefaultRouter()

router.register('todos',views.TodoViewSet,basename='todos-viewset')


urlpatterns = [  ] + router.urls