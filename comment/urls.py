from django.urls import path
from .views import *

urlpatterns = [
    path('add/<int:pk>', CommentListCreateForPost.as_view(), name='add_comment'),

]