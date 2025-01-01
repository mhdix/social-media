from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=25)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.slug} '   

    def get_absolute_url(self):
        return reverse('home:posts-detail', args=(self.id, self.slug))