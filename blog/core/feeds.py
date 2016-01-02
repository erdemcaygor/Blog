
# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from .models import Post
from taggit.models import Tag
from django.shortcuts import get_object_or_404


class LatestPosts(Feed):

    title = 'erdemcaygor.com: En Son Yazılar'
    link = '/'
    description = 'yeni yazı güncellemeleri'


    def items(self):

        return Post.active_objects.all()[:10]

    def item_title(self, item):

        return item.title

    def item_description(self, item):

        return item.content




class TagFeed(Feed):

    def get_object(self, request, tag):
        return get_object_or_404(Tag, name=tag)

    def title(self, obj):
        return "erdemcaygor.com %s ile ilgili makaleler" % obj.name

    def item_description(self, obj):
        return obj.content

    def link(self, obj):
        return "/#!tag/%s/" % obj.name

    def description(self, obj):
        return "%s ile ilgili tum yazilar" % obj.name

    def items(self, obj):

        return Post.active_objects.filter(tags__slug=obj.slug)














