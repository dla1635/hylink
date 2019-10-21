from rest_framework import serializers
from .models import Link 
from .models import Tag, LinkTag
from .models import Label, LinkLabel
from posts.models import UserSerializer as user


class LinkSerializer(serializers.ModelSerializer):
    user = user 

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
            'user'
        )
        read_only_fields = ('created_at',)


class TagSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields =(
            'id',
            'name',
            'links'
        )


class LabelSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Label
        fields = (
            'id',
            'name',
            'links'
        )

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
