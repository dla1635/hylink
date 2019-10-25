from rest_framework import serializers
from .models import Post 
from .models import PostComment
from .models import PostReport
from backend.links.models import Link 
from backend.links.serializers import LinkSerializer
from django.contrib.auth.models import User
# from django.conf import settings
# from django.contrib.auth import get_user_model
from backend.profiles.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)
    links = LinkSerializer(read_only=True, many=True)
    links_id = serializers.PrimaryKeyRelatedField(queryset=Link.objects.all(), write_only=True, many=True)
    like_users = UserSerializer(read_only=True, many =True)
    like_users_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, many=True)
    
    class Meta:
        model = Post
        fields = (
            'pk',
            'title',
            'contents',
            'links',
            'links_id',
            'created_at',
            'updated_at',
            'view_count',
            'like_count',
            'user',
            'like_users',
            'like_users_id'
        )
        read_only_fields = ('pk', 'created_at', 'updated_at',)


    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['user']


    def create(self, validated_data):
        links = validated_data.pop('links_id')
        posts = Post.objects.create(**validated_data)
        for lk in links:
            posts.links.add(lk)
        return posts 


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)
    post = PostSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)


    class Meta:
        model = PostComment
        fields = (
            'pk',
            'contents',
            'created_at',
            'updated_at',
            'user',
            'post',
            'post_id'
        )
        read_only_fields =('pk', 'created_at', 'updated_at',)


    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(CommentSerializer, self).get_validation_exclusions()

        return exclusions + ['user']


    def create(self, validated_data):
        post = validated_data.pop('post_id')
        comments = PostComment.objects.create(post=post, **validated_data)
        return comments



class ReportSerializer(serializers.ModelSerializer):
    report_users = UserSerializer(read_only=True, many=True)
    report_users_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, many=True)
    post = PostSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)
    

    class Meta:
        model = PostReport
        fields = (
            'pk',
            'contents',
            'created_at',
            'updated_at',
            'post',
            'post_id',
            'report_users',
            'report_users_id'
        )
        read_only_fields = ('pk', 'created_at', 'updated_at',)

    
    
    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ReportSerializer, self).get_validation_exclusions()

        return exclusions


    def create(self, validated_data):
        report_users = validated_data.pop('report_users_id')
        post = validated_data.pop('post_id')
        reports = PostReport.objects.create(post=post, **validated_data)
        for ru in report_users:
            reports.report_users.add(ru)
        return reports
