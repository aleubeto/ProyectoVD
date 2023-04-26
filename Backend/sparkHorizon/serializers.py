from rest_framework.serializers import ModelSerializer, ALL_FIELDS
from .models import Post,Gender,Usuario,TeamMember,Calificacion

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ALL_FIELDS


class GenderSerializer(ModelSerializer):
    class Meta:
        model = Gender
        fields = ALL_FIELDS

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ALL_FIELDS

class TeamSerializer(ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ALL_FIELDS

class CalificacionSerializer(ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ALL_FIELDS

class PostGetSerializer(ModelSerializer):
    genero = GenderSerializer()
    autores = TeamSerializer(many=True)
    calificaciones = CalificacionSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = ALL_FIELDS
