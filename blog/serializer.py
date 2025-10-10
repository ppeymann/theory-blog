from rest_framework import serializers

from comment.serializer import CommentSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'slug',
            'created_at',
            'updated_at',
            'published_at',
            'author',
            'status',
            'image',
            'comments'
        ]
        extra_kwargs = {
            'author': {'read_only': True},
        }
        read_only_fields = ['id', 'published_at','created_at', 'updated_at']