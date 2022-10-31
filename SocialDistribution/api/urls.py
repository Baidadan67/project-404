from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'authors', RestManyAuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
