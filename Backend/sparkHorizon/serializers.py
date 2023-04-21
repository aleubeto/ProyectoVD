from rest_framework.serializers import ModelSerializer, ALL_FIELDS
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model: Post
        fields: ALL_FIELDS