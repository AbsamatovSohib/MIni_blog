from rest_framework import serializers
from models import (
    Category, Post, Author
)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('title', 'image')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'text')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source="author.title")
    author_image = serializers.StringRelatedField(source="author.image")
    category = serializers.StringRelatedField(source="category.name")

    class Meta:
        model = Post
        fields = ('title', 'image', 'author', 'author_image', 'updated_at', 'category')

