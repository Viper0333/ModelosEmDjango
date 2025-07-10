# from django.shortcuts import render

# # Create your views here.

from django.views import generic
from .models import Post

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

