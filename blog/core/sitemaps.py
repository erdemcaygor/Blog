
# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSiteMap(Sitemap):

    changefreq = "never"
    priority = 0.5

    def items(self):

        return Post.active_objects.all()

    def lastmod(self, obj):

        return obj.created_date















