from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', "Draft"
        PUBLISHED = 'PB', "Published"
        REJECTED = 'RJ', "Rejected"

    title: str = models.CharField(max_length=250)
    description: str = models.TextField()
    slug: str = models.SlugField(max_length=250)

    # Date models
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    published_at: datetime = models.DateTimeField(default=timezone.now)

    # Related Field
    author: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')

    # Choice Field
    status: Status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()

    # for get just published Post
    published = PublishedManager()

    class Meta:
        ordering = ['-published_at']

        indexes = [
            models.Index(
                fields=['-published_at', 'title'],
            )
        ]

    def __str__(self):
        return self.title