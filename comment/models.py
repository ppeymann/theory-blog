from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from blog.models import Post

# Create your models here.

class Comment(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft',
        PUBLISHED = 'PB', 'Published',

    text:str = models.TextField()
    created_at:datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    status: Status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # relations
    author: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post: Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.text



