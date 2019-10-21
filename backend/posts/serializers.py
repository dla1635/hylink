from rest_framework import serializers
from .models import Post 
from .models import PostComment
from .models import PostReport
# from django.contrib.auth.models import User
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL,
        fields = ('id', 'email', 'nickname')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many =True)
    
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'contents',
            'created_at',
            'view_count',
            'like_count',
            'user',
            'like_users'
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

class ReportSerializer(serializers.ModelSerializer):
    report_users = UserSerializer(read_only=True, many=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = PostReport
        fields = (
            'id',
            'contents',
            'created_at',
            'post',
            'report_users'
        )
        read_only_fields = ('created_at',)
