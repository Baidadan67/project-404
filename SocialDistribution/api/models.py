from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AuthorManager
# Create your models here.

class Author(AbstractBaseUser, PermissionsMixin):
    
    type = models.CharField(default="authors", max_length=255)
    username = models.CharField(max_length=30, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    host = models.CharField(max_length=255, blank=True, default='http://127.0.0.1:8001/')
    
    displayName = models.CharField(max_length=255, null=True, blank=True)
    github = models.URLField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profileImage = models.URLField(max_length=255, blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        #return self.username
        return self.username

    @property
    def url(self):
        return self.host + "authors/" + str(self.id)
    objects = AuthorManager()