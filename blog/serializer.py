from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

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
        ]

        read_only_fields = ['id', 'published_at','created_at', 'updated_at'],