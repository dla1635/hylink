from rest_framework import serializers
from .models import Share, ShareLink
from django.conf import settings
from django.contrib.auth import get_user_model
from backend.profiles.serializers import UserSerializer
from backend.links.serializers import LinkSerializer


class ShareLinkSerializer(serializers.ModelSerializer):
    link = LinkSerializer()

    class Meta:
        model=ShareLink
        fields=(
            'id',
            'order',
            'link'
        )

class ShareSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    sharelink = ShareLinkSerializer(read_only=True, many=True)

    class Meta:
        model = Share
        fields=(
            'id',
            'user',
            'sharelink'
        )
