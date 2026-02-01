from rest_framework import viewsets
from .models import Movie
from .models import Director
from .serializers import MovieSerializer
from .serializers import DirectorSerializer
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['read', 'write']
    
    def get_permissions(self):
        if self.request.method =='GET':
            return [AllowAny()]
        self.required_scopes = ['write']
        return [IsAuthenticated(), TokenHasScope()]

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    
    authentication_classes = [OAuth2Authentication] 
    required_scopes = ['read', 'write']
    
    def get_permissions(self):
        if self.request.method =='GET':
            return [AllowAny()]
        self.required_scopes = ['write']
        return [IsAuthenticated(), TokenHasScope()]
