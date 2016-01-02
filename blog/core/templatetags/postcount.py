# -*- coding: utf-8 -*-

from django import template
from core.models import Post

register = template.Library()

@register.filter(name='postcount')
def postcount(category):

    posts = Post.active_objects.filter(category=category)
    count = len(posts)
    return count