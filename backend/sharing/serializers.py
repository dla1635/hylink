from rest_framework import serializers
from .models import Share, ShareLink
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
            'user',
            'title'
        )

class ShareLinkSerializer(serializers.ModelSerializer):
    link = LinkSerializer()
    share = ShareSerializer()

    class Meta:
        model=ShareLink
        fields=(
            'id',
            'order',
            'share',
            'link'
        )
