from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import render
from .models import *

# Create your views here.

# this function is for get pagination posts with specific page number
# and use it in index and post list function
def get_pagination_posts(request:WSGIRequest, per_page: int = 2):
    posts: QuerySet[Post]  = Post.published.all()
    paginator: Paginator = Paginator(posts, per_page)
    page_number: str | int = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return posts

def index(request:WSGIRequest):
    posts: QuerySet[Post] = get_pagination_posts(request)
    context = {
        'posts': posts,
    }

    return render(request, 'home/home.html', context)

def post_details(request: WSGIRequest, id):
    try:
        post: Post = Post.published.get(id=id)

    except:
        raise Http404('No Post Found!')

    context = {
        'post': post,
    }

    return render(request, '', context)

def post_list(request):
    posts: QuerySet[Post] = get_pagination_posts(request, 10)
    context = {
        'posts': posts,
    }

    # TODO: change this template route
    return render(request, 'home/home.html', context)


