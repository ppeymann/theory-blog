from django.shortcuts import render
from rest_framework import generics
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Post

# this view for show all post that published
class PostListView(generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = []

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)