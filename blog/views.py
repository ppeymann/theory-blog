from django.shortcuts import render
from rest_framework import generics
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post
from .permissions import IsAuthorOrReadOnly

# this view for show all post that published
class PostListView(generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = []

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class PostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]