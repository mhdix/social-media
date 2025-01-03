from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view() , name='home'),
    path('post/', views.PostView.as_view(), name="posts"),
    # path('user/<iny:user_id>', views.UserProfile.as_view(), name="user_profile"),
    path('post/<int:post_id>/<slug:post_slug>/', views.DetailView.as_view(), name="posts-detail"),
    path('delete/<int:post_id>/', views.DeletePostView.as_view(), name="post_delete"),
    path('post/update/<int:post_id>/', views.PostUpdateView.as_view(), name='post_update')
    
]
