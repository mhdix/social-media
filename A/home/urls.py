from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view() , name='home'),
    path('post/', views.PostView.as_view(), name="posts"),
    path('post/<int:post_id>/<slug:post_slug>/', views.DetailView.as_view(), name="posts-detail"),
]
