# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sitemaps import ping_google
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(_('Kategori'), max_length=50)
    is_active = models.BooleanField(_('Active'), default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_date',)




class postManager(models.Manager):

    def get_queryset(self):
        return super(postManager, self).get_queryset().filter(is_active=True, is_deleted=False)

class Post(models.Model):

    title = models.CharField(_('Başlık'), max_length=50)
    category = models.ForeignKey(Category)
    content = RichTextField()
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_('Active'), default=False)
    is_deleted = models.BooleanField(_('Silindi mi?'), default=False)
    objects = models.Manager()
    active_objects = postManager()
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return '#!/post/{0}/'.format(self.slug)


    class Meta:
        ordering = ('-created_date',)

def upload_to(instance, filename):

    return 'postimages/'+filename

class PostImages(models.Model):

    image = models.ImageField(upload_to=upload_to)
    post = models.ForeignKey(Post, related_name='images')






