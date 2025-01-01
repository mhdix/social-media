from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class HomeAdmin(admin.ModelAdmin):
    raw_id_field = ('user',)
    list_filter = ('created_at','updated_at')
    list_display = ('title','created_at','updated_at', 'id')  
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('user', 'title')