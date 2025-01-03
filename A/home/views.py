from django.contrib.auth.forms import User
from django.shortcuts import redirect, render
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostUpdateForm
from django.utils.text import slugify
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

class DetailView(View):
    def get(self, req, post_id, post_slug):
        post = Post.objects.get(id=post_id, slug=post_slug)
        return render(req, 'home/detail.html', {'post': post})
        

class DeletePostView(LoginRequiredMixin, View):
    def get(self, req, post_id):
        post = Post.objects.get(pk=post_id)
        if post.user.id == req.user.id:
            post.delete()
            messages.success(req, 'deleted item successfuly', 'success')
        else:
            messages.error(req, 'you cant delete this post', 'error')
        return redirect('home:home')


class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostUpdateForm

    def setup(self, req, *args, **kwargs):
        self.psot_instance = Post.objects.get(pk=kwargs['post_id'])
        return super().setup(req, *args, **kwargs)
        
    def dispatch(self, req, *args, **kwargs):
        post = self.psot_instance
        if not post.user.id == req.user.id:
            messages.error(req, 'you cant update this post')
            return redirect('home:home')
        return super().dispatch(req, *args, **kwargs)

    def get(self, req, *args, **kwargs):
        post = self.psot_instance
        form = self.form_class( instance=post)
        return render(req, 'home/update.html', {'form':form})
                
    def post(self, req, *args, **kwargs):
       post = self.psot_instance
       form = self.form_class(req.POST, instance=post)
       if form.is_valid():
           new_post = form.save(commit=False)
           new_post.slug = slugify(form.cleaned_data['description'][:30])
           new_post.save()
           messages.success(req, 'form updated successfuly', 'success')
           return redirect('home:posts-detail', post.id, post.slug)