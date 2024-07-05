from django.contrib import admin

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'views')
    search_fields = ('title', 'content')
    list_filter = ('published_date', 'author')


admin.site.register(BlogPost, BlogPostAdmin)
