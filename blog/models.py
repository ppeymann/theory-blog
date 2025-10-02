from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManage(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT: str = 'DF', 'Draft'
        PUBLISHED: str = 'PB', 'Published'
        REJECTED: str = 'RJ', 'Rejected'

    # Related with user table
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')


    # title of post
    title: str = models.CharField(max_length=250)
    # description of post
    description: str = models.TextField()
    # slug of post
    slug:str = models.SlugField(max_length=250)

    # Date
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManage()

    class Meta:
        ordering = ['-publish']

        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title