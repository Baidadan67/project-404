from rest_framework import serializers
from . models import *

class restManyAuthorSerializer(serializers.ModelSerializer):
    type = serializers.CharField()
    url = serializers.CharField()
    
    class Meta:
        model = Author
        fields = ["type","id","host","displayName","url","github","profileImage"]