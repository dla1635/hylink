from .serializers import LinkSerializer, TagSerializer, LabelSerializer
from .serializers import LinkTagSerializer, LinkTagDetailSerializer, LinkLabelSerializer, LinkLabelDetailSerializer
from .models import Link, Tag, Label, LinkTag, LinkLabel
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.db.models import Count, F

# from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework import status, viewsets
# from rest_framework.filters import OrderingFilter
# from rest_framework.response import Response


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update_linktag(self, link, user_tags):
        if user_tags != None:
            if Tag.objects.all().count() > 0:
                tags = Tag.objects.all()
                for user_tag in user_tags:
                    hasTag = False
                    for tag in tags:
                        if tag.name == user_tag:
                            hasTag = True
                            break
        
                if hasTag == False:
                    Tag(name=user_tag).save()

                link_tag = Tag.objects.get(name=user_tag)
                link.tag.add(link_tag)
            else:
                for user_tag in user_tags:
                    link_tag = Tag(name=user_tag)
                    link_tag.save()
                    link.tag.add(link_tag)
        else:
            print("TAG가 없습니당")
    
    # =============links=============
    # user별로 links list 보내주는 methods
    def list(self, request):
        user_links = Link.objects.all().filter(user=self.request.user)
        serializer = self.get_serializer(user_links, many=True)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # =============link=============

    # POST
    def create(self, request):
        print("here~~")
        # 1. request에 담긴 link정보 가져오기
        user = request.user
        url = request.data.get('url', None)
        title = request.data.get('title',None)
        thumbnail = request.data.get('thumbnail',None)
        summary = request.data.get('summary',None)
        sharable = 0

        print(url+" "+title+" "+thumbnail+" "+summary)

        new_link = Link(user=user, url=url, title=title, thumbnail=thumbnail, summary=summary, sharable=sharable)
        new_link.save()

        # Movie.objects.filter(id=id).count()
        user_tags = request.data.get('tags', None)
        print("================")
        self.update_linktag(new_link, user_tags)
        # if user_tags != None:
        #     if Tag.objects.all().count() > 0:
        #         tags = Tag.objects.all()
        #         for user_tag in user_tags:
        #             hasTag = False
        #             for tag in tags:
        #                 if tag.name == user_tag:
        #                     hasTag = True
        #                     break
        
        #         if hasTag == False:
        #             Tag(name=user_tag).save()

        #         link_tag = Tag.objects.get(name=user_tag)
        #         new_link.tag.add(link_tag)
        #     else:
        #         for user_tag in user_tags:
        #             link_tag = Tag(name=user_tag)
        #             link_tag.save()
        #             new_link.tag.add(link_tag)
        # else:
        #     print("TAG가 없습니당")

        #########################################################################
        # default로 들어와야 하는 값이 없을 경우, 처리 해야 됨. 에러 메세지 보내기!! #
        #########################################################################
        return Response(status=status.HTTP_200_OK)

    # PUT
    def update(self, request):
        l_id = request.data.get('l_id', None)

        if Link.objects.get(id=l_id).count() != 0:
            user = request.user
            url = request.data.get('url', None)
            title = request.data.get('title',None)
            thumbnail = request.data.get('thumbnail',None)
            summary = request.data.get('summary',None)
            sharable = request.data.get('sharable',None)
            if sharable != None:
                sharable = int(sharable)

            update_link = Link.objects.get(id=l_id)
            update_link.url = url
            update_link.title = title
            update_link.thumbnail = thumbnail
            update_link.summary = summary
            update_link.sharable = sharable

            user_tags = request.data.get('tags', None)
            update_linktag(update_link, user_tags)
        else:
            print("링크가 존재하지 않아 수정할 수 없습니다.")
        # user_tags = request.data.get('tags', None)
        # update_linktag(new_link, user_tags)
        # tags = Tag.objects.all()
        # for user_tag in user_tags:
        #     hasTag = False
        #     for tag in tags:
        #         if tag.name == user_tag:
        #             hasTag = True
        #             break
    
        #     if hasTag == False:
        #         Tag(name=user_tag).save()

        #     link_tag = Tag.objects.get(name=user_tag)

        #     # tag를 clear하는 방법
        #     update_link.tag.add(link_tag)

        # if sharable != None:
        #     sharable = int(sharable)
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request):
        return Response(status=status.HTTP_200_OK)
    # def retrieve(self, request):
    #     # Link, Tag, Label
    #     l_id = request.GET.get('l_id', None)
    #     u_id = request.GET.get('u_id',None)

    #     if l_id != None or u_id != None:
    #         link = Link.objects.get(id=l_id, user=u_id)
    #         tags = Tag.objects.filter(link=l_id)
                                                                                                                      
    #     else:
    #         print("RETRIEVE ERROR\n NOT EXIT LINK DATA")
    #     link = Link.objects.get(id=l_id)
    #     t_id = LinkTag.objects.filter(link=l_id)

    #     user_links = Link.objects.all().filter(user=self.request.user)
    
    # def update(self, request):
    #     user_links = Link.objects.all().filter(user=self.request.user)
    
    # def destroy(self, request):
    #     return super().destroy(request)
    


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        print("linklist GET")
        user = request.user
        print(user)
        link_list = Link.objects.all().filter(user=user)
        print(link_list)
        serializer = LinkSerializer(link_list, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
# class  (viewsets.ModelViewSet):
#     queryset = Label.objects.all()
#     serializer_class = LabelSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)       

# class LinkLabelViewSet(viewsets.ModelViewSet):
#     queryset = LinkLabel.objects.all()
#     serializer_class = LinkLabelSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

        
# class LinkTagViewSet(viewsets.ModelViewSet):
#     queryset = LinkTag.objects.all()
#     serializer_class = LinkTagSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
# class LinkTagViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     Return the given match.
#     list:
#     Return a list of all the existing matches.
#     create:
#     Create a new match instance.
#     """
#     queryset = LinkTag.objects.all()
#     serializer_class = LinkTagSerializer # for list view
#     detail_serializer_class = LinkTagDetailSerializer # for detail view
#     filter_backends = (DjangoFilterBackend, OrderingFilter,)
#     ordering_fields = '__all__'
#     def get_serializer_class(self):
#         """
#         Determins which serializer to user `list` or `detail`
#         """
#         if self.action == 'retrieve':
#             if hasattr(self, 'detail_serializer_class'):
#                 return self.detail_serializer_class
#         return super().get_serializer_class()
#     def get_queryset(self):
#         """
#         Optionally restricts the returned queries by filtering against
#         a `sport` and `name` query parameter in the URL.
#         """
#         queryset = LinkTag.objects.all()
#         link = self.request.query_params.get('link', None)
#         tag = self.request.query_params.get('tag', None)
#         if link is not None:
#             link = link.title()
#             queryset = queryset.filter(link__name=link)
#         if tag is not None:
#             queryset = queryset.filter(tag=tag)
#         return queryset
#     def create(self, request):
#         """
#         to parse the incoming request and create a new match or update
#         existing odds.
#         """
#         message = request.data.pop('message_type')
#         # check if incoming api request is for new event creation
#         if message == "NewEvent":
#             event = request.data.pop('event')
#             sport = event.pop('sport')
#             markets = event.pop('markets')[0] # for now we have only one market
#             selections = markets.pop('selections')
#             sport = Sport.objects.create(**sport)
#             markets = Market.objects.create(**markets, sport=sport)
#             for selection in selections:
#                 markets.selections.create(**selection)
#             match = Match.objects.create(**event, sport=sport, market=markets)
#             return Response(status=status.HTTP_201_CREATED)
#         # check if incoming api request is for updation of odds
#         elif message == "UpdateOdds":
#             event = request.data.pop('event')
#             markets = event.pop('markets')[0]
#             selections = markets.pop('selections')
#             for selection in selections:
#                 s = Selection.objects.get(id=selection['id'])
#                 s.odds = selection['odds']
#                 s.save()
#             match = Match.objects.get(id=event['id'])
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)