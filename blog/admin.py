from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ['author']

