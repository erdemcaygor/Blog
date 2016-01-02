
# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
                        url('^posts/$', PostList.as_view(), name='PostList'),
                        url('^categories/$', CategoryList.as_view(), name='CategoryList'),
                        url('^category-posts/(?P<name>\w+)/$', CategoryPosts.as_view(), name='CategoryPosts'),
                        url('^post/(?P<slug>[-\w]+)/$', PostDetail.as_view(), name='PostDetail'),
                        url('^tag/(?P<slug>[-\w]+)/$', TaggedPosts.as_view(), name='TaggedPosts'),
                        url('^posttags/(?P<slug>[-\w]+)/$', PostTags.as_view(), name='PostTags'),
                        url('^search/$', Search.as_view(), name='Search'),
                        url('^mail/$', Email.as_view(), name='Email'),
                      )