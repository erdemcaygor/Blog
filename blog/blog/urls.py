from django.conf.urls import include, url
from django.contrib import admin
from core.views import Home
from django.conf import settings
from django.conf.urls.static import static
from core.sitemaps import PostSiteMap
from core.feeds import LatestPosts, TagFeed

sitemaps = {
    'posts': PostSiteMap,
    'tags': TagFeed
}

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='Home'),
    url(r'^grappelli', include('grappelli.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^feed/$', LatestPosts()),
    url(r'^feed/tag/(?P<tag>[-\w]+)/$', TagFeed()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













