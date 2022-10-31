from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import restManyAuthorSerializer
# Create your views here.

class RestManyAuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = restManyAuthorSerializer
    permission_classes = [permissions.IsAuthenticated]