# -*- coding:utf-8 -*-

from core.models import Post, Category
from rest_framework import serializers
from taggit.models import Tag

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Post















