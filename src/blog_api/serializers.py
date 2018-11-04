from rest_framework import serializers
from .models import Author, Category, Post
from django.db import models

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'alias', 'name', 'photo', 'created', 'modified')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'created', 'modified')

class PostSerializer(serializers.ModelSerializer):

    image_450 = serializers.ImageField(allow_empty_file=True, required=False)

    class Meta:
        model = Post
        fields = (
                    'id',
                    'title',
                    'slug',
                    'status',
                    'category',
                    'content',
                    'image',
                    'image_450',
                    'author',
                    'created',
                    'modified',
                    'categoryName',
                    'authorName',
                )
