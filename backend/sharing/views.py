from .serializers import LinkGroupSerializer, ShareSerializer
from .models import LinkGroup, Share
from ..links.models import Link
from django.contrib.auth import get_user_model

from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count, F, Q

class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request):
        return Response(status=status.HTTP_200_OK)