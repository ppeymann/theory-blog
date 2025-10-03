from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('add/', PostCreateView.as_view(), name='add'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]