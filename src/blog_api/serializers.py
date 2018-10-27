from rest_framework import serializers
from .models import Author, Category, Post

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'alias', 'name', 'photo', 'created', 'modified')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'created', 'modified')

class PostSerializer(serializers.ModelSerializer):

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
                    'author',
                    'created',
                    'modified'
                )
