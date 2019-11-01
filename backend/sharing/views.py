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
        user = request.user
        link_list = request.data.get('link_list', None)
        ###### user & linklist 유효성 검사 ######

        # 1. Share 객체 만들기
        new_share = Share(user=user)
        new_share.save()

        for l_id in link_list:
            link = Link.objects.get(id=l_id)
            LinkGroup(group=new_share, link=link).save()

        return Response(status=status.HTTP_200_OK)