from rest_framework import serializers
from .models import *

class Image_Base64Serializer(serializers.ModelSerializer):
    class Meta:
        model= Image_Base64
        fields= '__all__'
