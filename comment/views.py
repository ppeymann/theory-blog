from django.shortcuts import render, get_object_or_404
from .models import Comment
from .serializer import CommentSerializer
from .permission import IsOwnerOrReadOnly
from blog.models import Post
from rest_framework.exceptions import NotFound
from rest_framework import generics, permissions
# Create your views here.

class CommentListCreateForPost(generics.ListCreateAPIView):
    serializer_class: CommentSerializer = CommentSerializer
    permission_classes: list = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return Comment.objects.filter(post__id=post_id)


    def perform_create(self, serializer):
        post_id = self.kwargs.get("pk")
        post:Post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)