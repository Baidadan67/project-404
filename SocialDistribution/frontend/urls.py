from urllib.parse import urlparse
from django.urls import path, include


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]

