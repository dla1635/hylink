from .serializers import ShareLinkSerializer, ShareSerializer, UrlSerializer
from .models import ShareLink, Share
from ..links.models import Link
from django.contrib.auth import get_user_model

from rest_framework import permissions, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count, F, Q

# from rest_framework.decorators import authentication_classes, permission_classes

# @api_view(['POST'])    
# @authentication_classes([])
# @permission_classes([])
# def items(request):
#    return Response({"message":"Hello world!"})

# def get_context_data():
#     sharelinks = Share.objects.annotate(link)
def isvalid_user(user):
    valid = True if get_user_model().objects.filter(id=user.id).count() > 0 else False
    print(valid)
    msg = "user valid" if valid == True else "user invalid"
    return valid, msg

def isvalid_link(link_list):
    for link_id in link_list:
        valid = True if Link.objects.filter(id=link_id).count() > 0 else False
        if not valid:
            return valid, "link invalid"   
    return True, "link_list valid"

def isvalid_share(share_id):
    valid = True if Share.objects.filter(id=share_id).count() > 0 else False
    msg = "share valid" if valid == True else "share invalid"
    return valid, msg
        
@permission_classes((AllowAny, ))
class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def create(self, request):
        user = request.user
        valid, msg = isvalid_user(user)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK)

        link_list = request.data.get('link_list', None)
        valid, msg = isvalid_link(link_list)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK)
        
        ###### user & linklist 유효성 검사 ######

        # 1. Share 객체 만들기
        new_share = Share(user=user)
        new_share.save()

        for order, l_id in enumerate(link_list):
            link = Link.objects.get(id=l_id)
            link_share = ShareLink(order=order, link=link)
            link_share.save()
            new_share.sharelink.add(link_share)
        
        serializer = ShareSerializer(new_share, many=False)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    # def list(self, request, pk):
    #     print(type(pk))
    #     print("here")
    #     # s_id = request.data.GET('id', None)
    #     # valid, msg = isvalid_share(s_id)
    #     # if not valid:
    #     #     print(msg)
    #     #     return Response(status=status.HTTP_200_OK)
    #     # share = Share.objects.get(id=pk)
    #     link_list = ShareLink.objects.filter().order_by('order')
    #     serializer = ShareLinkSerializer(link_list, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    

