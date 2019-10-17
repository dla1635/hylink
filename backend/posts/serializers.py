from rest_framework import serializers
from .models import Post 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

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