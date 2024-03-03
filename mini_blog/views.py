from django.shortcuts import render
from rest_framework import generics
from .models import Category, Post, Author
from .serializer import PostSerializer

# Create your views here.


class FeaturedThisView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_featured=True)[:2]


