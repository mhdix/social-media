from django.contrib.auth.forms import User
from django.shortcuts import render
from django.views import View
from .models import Post
# Create your views here.


class HomeView(View):
    def get(self, req):
        return render(req, 'home/index.html')



class PostView(View):
    def get(self, req):
        posts = Post.objects.all()
        return render(req, 'home/post.html', {'posts' : posts})
    
    def post(self, req):
        return render(req, 'home/index.html')
    
# class PostDetailView(View):
#     def get(self, req):
#         return render(req, 'home/detail.html')


class DetailView(View):
    def get(self, req, post_id, post_slug):
        post = Post.objects.get(id=post_id, slug=post_slug)
        return render(req, 'home/detail.html', {'post': post})
        
