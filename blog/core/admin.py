# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Post, Category, PostImages

class PostImagesInline(admin.TabularInline):
    model = PostImages
    extra = 5

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'is_active', 'is_deleted']
    inlines = [ PostImagesInline, ]
    list_filter = ['is_deleted', 'is_active']
    prepopulated_fields = {
        'slug': ('title',)
    }

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'is_active']
    list_filter = ['is_active']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)