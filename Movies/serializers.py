from rest_framework import serializers
from .models import Movie
from .models import Director
from django.core.files.base import ContentFile
import base64 

class MovieSerializer(serializers.ModelSerializer): 
    
    picture = serializers.CharField(required=False, allow_blank=True)
       
    class Meta:
        model = Movie
        fields = '__all__'
    
    def validate_picture(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            except Exception:
                raise serializers.ValidationError("La imagen no es valida.")
        return value

class DirectorSerializer(serializers.ModelSerializer): 
    movies = MovieSerializer(many=True, read_only=True)
    picture = serializers.CharField(required=False, allow_blank=True)
       
    class Meta:
        model = Director
        fields = '__all__'
    
    def validate_picture(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            except Exception:
                raise serializers.ValidationError("La imagen no es valida.")
        return value