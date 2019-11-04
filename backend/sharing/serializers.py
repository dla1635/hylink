from rest_framework import serializers
from .models import Share, LinkGroup
from django.conf import settings
from django.contrib.auth import get_user_model
from backend.profiles.serializers import UserSerializer
from backend.links.serializers import LinkSerializer

class ShareSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Share
        fields=(
            'id',
            'user'
        )

class LinkGroupSerializer(serializers.ModelSerializer):
    link = LinkSerializer(read_only=True)
    group = ShareSerializer(read_only=True)

    class Meta:
        model=LinkGroup
        fields=(
            'id',
            'group',
            'link'
        )