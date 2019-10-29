from .serializers import LinkSerializer, TagSerializer, LabelSerializer
from .serializers import LinkTagSerializer, LinkTagDetailSerializer, LinkLabelSerializer, LinkLabelDetailSerializer
from .models import Link, Tag, Label, LinkTag, LinkLabel
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count, F, Q
from django.contrib.auth.models import User 
# from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework import status, viewsets
# from rest_framework.filters import OrderingFilter
# from rest_framework.response import Response


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    '''
    link 객체와 user tag를 인자로 받아 
    Tag table에 없는 user tag는 create하고 link 객체와 연결
    '''
    def update_linktag(self, link, user_tags):
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

        # if user_tags != None:

        #     tags = Tag.objects.all()

        #     for user_tag in user_tags:
        #        hasTag = False
        #         for tag in tags:
        #             if tag.name == user_tag:
        #                 hasTag = True
        #                 break
        #         if hasTag == False:
        #             Tag(name=user_tag).save()
        #         link_tag = Tag.objects.get(name=user_tag)
        #         link.tag.add(link_tag)    
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
        #         link.tag.add(link_tag)
        #     else:
        #         for user_tag in user_tags:
        #             link_tag = Tag(name=user_tag)
        #             link_tag.save()
        #             link.tag.add(link_tag)
        # else:
        #     print("TAG가 없습니당")

    def isvalid_value(self, user, url, title, thumbnail, summary, visible):
        msg = ""
        if user == None:
            msg += 'user '
        
        if url == None:
            msg += 'url '

        if title == None:
            msg += 'title '

        if thumbnail == None:
            msg += 'thumbnail '

        if summary == None:
            msg += 'summary '
    
    def isvalid_link(self, l_id):
        valid = True if Link.objects.get(id=l_id).count() > 0 else False
        msg = "link valid" if valid == True else "link invalid"
        return valid, msg

    def isvalid_user(self, user):
        valid = True if User.objects.get(user=user).count() > 0 else False
        msg = "user valid" if valid == True else "user invalid"
        return valid, msg
    
    def isvalid_label(self, label):
        valid = True if Label.objects.get(name=label).count() > 0 else False
        msg = "label valid" if valid == True else "label invalid"
        return valid, msg
    '''
    [method] = POST
    입력값으로 link 생성한 뒤, DB에 저장
    tag가 입력됐다면 tag저장 후, link와 연결
    '''
    def create(self, request):
        print("link create")
        user = request.user
        # user가 유효한지 확인 
        valid, msg = self.isvalid_user(user)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK) 

        url = request.data.get('url', None)
        title = request.data.get('title',None)
        thumbnail = request.data.get('thumbnail',None)
        summary = request.data.get('summary',None)
        sharable = 0
        # value가 유효한지 확인
        # isvalid_value()
        print(url+" "+title+" "+thumbnail+" "+summary)

        # summary, thumbnail, tag 가져오는 method function(url)

        new_link = Link(user=user, url=url, title=title, thumbnail=thumbnail, summary=summary, sharable=sharable)
        new_link.save()

        user_tags = request.data.get('tags', None)
        self.update_linktag(new_link, user_tags)

        return Response(status=status.HTTP_200_OK)

    # PUT
    def update(self, request):
        l_id = request.data.get('l_id', None)
        # 유효한 link인지 확인
        valid, msg = self.isvalid_link(l_id)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK)

        user = request.user
        # user가 유효한지 확인 
        valid, msg = self.isvalid_user(user)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK) 

        url = request.data.get('url', None)
        title = request.data.get('title',None)
        thumbnail = request.data.get('thumbnail',None)
        summary = request.data.get('summary',None)
        sharable = request.data.get('sharable',None)
        if sharable != None:
            sharable = int(sharable)
        # value가 유효한지 확인
        # isvalid_value()

        update_link = Link.objects.get(id=l_id)
        update_link.url = url
        update_link.title = title
        update_link.thumbnail = thumbnail
        update_link.summary = summary
        update_link.sharable = sharable

        user_tags = request.data.get('tags', None)
        update_linktag(update_link, user_tags)

        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request):

        return Response(status=status.HTTP_200_OK)
    
    def destroy(self, request):
        l_id = request.data.get('l_id', None)
        # 유효한 link인지 확인
        valid, msg = self.isvalid_link(l_id)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK)

        Link.object.get(id=l_id).delete()
        
        return Response(status=status.HTTP_200_OK)


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        print("linklist GET")
        user = request.user
        valid, msg = self.isvalid_user(user)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK)

        search_type = request.data.get('type',None)
        if search_type != 'tag' or search_type != None or search_type != 'label' or search_type != 'word':
            print("잘못된 입력으로 검색했습니다.")
            return Response(status=status.HTTP_200_OK)

        word = request.data.get('word', None)
        if word == None:
            print("검색 단어가 입력되지 않았습니다.")
            return Response(status=status.HTTP_200_OK)
        
        link_list = Link.objects.all().filter(user=user)

        if search_type != None: # ALL
            result = link_list
        elif search_type == 'word': # search word를 포함한 links
            # content_filter = link_list.filter(Q(summary__icontains=word)|Q(title__icontains=word)) if link_list.filter(Q(summary__icontains=word)|Q(title__icontains=word)).count() > 0 else None
            content_filter = link_list.filter(Q(summary__icontains=word)|Q(title__icontains=word))
            tag_filter = Tag.objects.get(name=word).links.all().filter(user=user)
            result = content_filter.union(tag_filter, all=False)
        elif search_type == 'tag': # tag를 포함한 links
            result =  Tag.objects.get(name=word).links.all().filter(user=user)
        elif search_type == 'label': # label에 포함된 links
            result = Label.objects.get(name=word).links.all().filter(user=user)

        # link_list = Link.objects.all()
        serializer = LinkSerializer(result, many=True)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def create(self, request):
        print("Label create")

        label = request.data.get('label', None)

        if label != None and Label.objects.get(name=label).count == 0:
            Label(name=label).save()
        else:
            print("이미 존재하는 label 또는 label 값이 제대로 입력되지 않음")
    
        return Response(status=status.HTTP_200_OK)
    
    def update(self, request):
        print("label update")

        l_id = request.data.get('l_id', None)
        name = request.data.get('name', None)
        update_label = Link.objects.get(id=l_id)
        update_label.name = name
        

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