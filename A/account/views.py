from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
 
class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'account/register.html'  


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs) 
        
    
    
    def get(self, req):
        form = self.form_class
        return render(req, self.template_name, {'form':form})

    def post(self, req):
        form=UserRegisterForm(req.POST)
        print(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(req, 'your register successfuly', 'success')
            return redirect('home:home')
        return render(req , self.template_name, {'form':form})



class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    
    
    def dispatch(self, req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(req, *args, **kwargs)
        

    def get(self, req):
        form = self.form_class
        return render(req, self.template_name, {'form' : form})

    def post(self, req):
        form = self.form_class(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(req, username=cd['username'], password=cd['password'])
            if user is not None:
                login(req, user)
                messages.success(req, 'login is success', 'success')
                return redirect('home:home')
            messages.error(req, 'username or pass is wrong', 'warning')
        return render(req, self.template_name, {'form':form} )
    
    
class UserLogoutView(LoginRequiredMixin, View):
    def get(self, req):
        logout(req)
        messages.success(req, 'your logout success', 'success')
        return redirect('home:home')