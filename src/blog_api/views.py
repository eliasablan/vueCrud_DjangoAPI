from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Author, Category, Post
from .serializers import AuthorSerializer, CategorySerializer, PostSerializer

class AuthorAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostAPI(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
