from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'public', 'slug')
    list_filter = ('public',)
    search_fields = ('title','descriptions',)
    prepopulated_fields = {'slug': ('title',)}