from rest_framework import serializers
from .models import Post 
from .models import PostComment
# from django.contrib.auth.models import User
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL,
        fields = ('id', 'email', 'nickname')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'contents',
            'created_at',
            'view_count',
            'like_count',
            'user'
        )
        read_only_fields = ('created_at',)

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = (
            'id',
            'contents',
            'created_at',
            'user',
            'post'
        )
        read_only_fields =('created_at',)