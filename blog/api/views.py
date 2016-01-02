# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from core.models import Post, Category
from django.db.models.query import Q
from .serializers import PostSerializer, CategorySerializer, TagSerializer
from django.core.mail import send_mail


class PostList(ListAPIView):

    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.active_objects.all()


class CategoryList(ListAPIView):

    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()




class CategoryPosts(ListAPIView):

    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        category_name = self.kwargs.get('name')
        category = Category.objects.get(name=category_name)
        return Post.active_objects.filter(category=category)


class PostDetail(ListAPIView):

    def get(self, request, *args, **kwargs):

        slug = self.kwargs.get('slug')
        post = Post.active_objects.get(slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)



class TaggedPosts(ListAPIView):

    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Post.active_objects.filter(tags__slug=slug)


class PostTags(ListAPIView):

    serializer_class = TagSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        post = Post.active_objects.get(slug=slug)
        return post.tags.all()


class Search(ListAPIView):

    model = Post
    serializer_class = PostSerializer
    queryset = Post.active_objects.all()

    def get_queryset(self):

        qs = super(Search, self).get_queryset()
        search_data = self.request.query_params.get('search_data', None)
        if search_data:
            qs = qs.filter(Q(title__icontains=search_data) | Q(content__icontains=search_data) | Q(category__name__icontains=search_data))
        return qs


class Email(APIView):
    parser_classes = (JSONParser,)
    def post(self, request, *args, **kwargs):

        data = request.data
        message = data.get('message')
        subject = message.get('subject')
        content = message.get('content')
        email_address = message.get('email')
        try:
            send_mail(subject, content, email_address, ['admin@example.com'])
        except:
            return Response(False, status=status.HTTP_400_BAD_REQUEST)
        return Response(True, status=status.HTTP_200_OK)














