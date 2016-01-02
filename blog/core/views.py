
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext
from .models import Category, Post
from taggit.models import Tag


class Home(View):

    def get(self, request):
        categories = Category.objects.all()
        tags = Tag.objects.all()
        last_posts = Post.active_objects.all()[:5]
        return render_to_response('home.html', locals(), context_instance=RequestContext(request))