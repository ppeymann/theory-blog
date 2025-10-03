from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('add/', PostCreateView.as_view(), name='add'),

]