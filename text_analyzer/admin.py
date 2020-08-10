from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['word', 'count']
    list_filter = ['word', 'count']


admin.site.register(Post, PostAdmin)
