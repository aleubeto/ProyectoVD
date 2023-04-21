from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import *

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class GenderViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = GenderSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UsuarioSerializer

class TeamViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = TeamSerializer

class CalificacionViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CalificacionSerializer