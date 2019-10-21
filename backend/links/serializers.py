from rest_framework import serializers
from .models import Link 
from .models import Tag, LinkTag
from .models import Label, LinkLabel
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL,
        fields = ('id', 'email', 'nickname')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields =(
            'id',
            'name',
            'links'
        )


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = (
            'id',
            'name',
            'links'
        )


class LinkSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tag = TagSerializer(read_only=True, many=True)
    label = LabelSerializer(read_only=True, many=True)

    class Meta:
        model = Link
        fields = (
            'id',
            'url',
            'title',
            'thumbnail',
            'summary',
            'sharable',
            'created_at',
            'updated_at',
            'user',
            'tag',
            'label',
        )
        read_only_fields = ('created_at', 'updated_at',)
        

class LinkTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkTag
        fields = (
            'id',
            'url',
            'date_joined'
        )

class LinkLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkLabel
        fields = (
            'id',
            'url',
            'date_joined'
        )

class LinkTagDetailSerializer(serializers.ModelSerializer):
    link = LinkSerializer()
    tag = TagSerializer()
    class Meta:
        model = LinkTag
        fields = (
            'id',
            'url',
            'date_joined',
            'link',
            'tag'
        )


class LinkLabelDetailSerializer(serializers.ModelSerializer):
    link = LinkSerializer()
    label = LabelSerializer()
    class Meta:
        model = LinkLabel
        fields = (
            'id',
            'url',
            'date_joined',
            'link',
            'label'
        )
