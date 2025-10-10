from django.urls import path
from .views import *

urlpatterns = [
    path('add/<int:pk>/', CommentListCreateForPost.as_view(), name='add_comment'),
    path('update/<int:pk>/', CommentUpdate.as_view(), name='update_comment'),
    path('delete/<int:pk>/', CommentDelete.as_view(), name='delete_comment'),

]