from .serializers import LinkSerializer, TagSerializer, LabelSerializer
from .serializers import LinkTagSerializer, LinkTagDetailSerializer, LinkLabelSerializer, LinkLabelDetailSerializer
from .models import Link, Tag, Label, LinkTag, LinkLabel
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count, F, Q
from .textrankr import TextRank
from .url2text import urlparse
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

# from django_filters.rest_framework import DjangoFilterBackend 
# from rest_framework.filters import OrderingFilter

def isvalid_value(user, url, title, thumbnail, summary, visible):
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

def isvalid_link(l_id):
    valid = True if Link.objects.filter(id=l_id).count() > 0 else False
    msg = "link valid" if valid == True else "link invalid"
    return valid, msg

def isvalid_user( user):
    valid = True if get_user_model().objects.filter(id=user.id).count() > 0 else False
    print(valid)
    msg = "user valid" if valid == True else "user invalid"
    return valid, msg

def isvalid_label(lb_id):
    valid = True if Label.objects.filter(id=lb_id).count() > 0 else False
    msg = "label valid" if valid == True else "label invalid"
    return valid, msg

@permission_classes((AllowAny, ))
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    '''
    link 객체와 user tag를 인자로 받아 
    Tag table에 없는 user tag는 create하고 link 객체와 연결
    '''
    def update_linktag(self, link, tags_name):
        tags = Tag.objects.all()
        link.tag.all().delete()

        for tag_name in tags_name:
            hasTag = False
            for tag in tags:
                if tag.name == tag_name:
                    hasTag = True
                    break
            if hasTag == False:
                Tag(name=tag_name).save()
            link_tag = Tag.objects.get(name=tag_name)
            link.tag.add(link_tag)    

    def update_linklabel(self, link, labels_name, user):
        labels = Label.objects.filter(user=user)
        link.label.all().delete()

        for label_name in labels_name:
            hasLabel = False
            for label in labels:
                if label.name == label_name:
                    hasLabel = True
                    break
            
            if hasLabel == False:
                Label(name=label_name, user=user).save()
            
            link_label = Label.objects.get(name=label_name)
            link.label.add(link_label)
    def link_create(self, user, url, is_visible):
        # 3. url로 썸네일, 태그, 제목, 3줄 요약 가져오기
        thumbnail, title, input_text, meta_tag = urlparse(url) # string으로 None이 넘어올 수 있음
        print(meta_tag)

        if title=='None':
            print("유효하지 않는 URL")
            return False
        
        textrank = TextRank(input_text) #TextRank생성되면서 내부에서 요약, 키워드 처리함
        sentences = textrank.summarize(3, verbose=False) #sentences에 list형식으로 3개 돌려줌 verbose는 \n 추가할지 여부인데 필요없을듯
        if len(meta_tag) > 1:
            keywords = meta_tag
        else:
            keywords = textrank.keywords(3) #keyword 3개 list형식, 다만 키워드값은 [idx][0]번째에 저장되있음

        print(keywords)
        # 4. 가져온 태그와 3줄 요약 정리
        user_tags =[]
        for i in range(0,3):
            keyword = keywords[i]
            if keyword != 'None':
                user_tags.append(keyword)
        
        print(user_tags)
        summary = ''
        for i in range(0,3):
            sentence = sentences[i]
            if sentence != 'None':
                summary += (sentence+' ')
        
        if summary == '':
            summary = 'None'

        # value가 유효한지 확인
        # isvalid_value()
        print(url+" "+title+" "+thumbnail+" "+summary)

        # 5. link 객체 생성후, DB에 저장
        new_link = Link(user=user, url=url, title=title, thumbnail=thumbnail, summary=summary, sharable=0, is_visible=is_visible)
        new_link.save()

        self.update_linktag(new_link, user_tags)
        return True
    
    def link_update(self, l_id, user, title, thumbnail, summary, is_visible,link_tags, link_labels):
        update_link = Link.objects.get(id=l_id)
        # update_link.url = url
        update_link.title = title
        
        if is_visible == 1 or is_visible == 3:
            update_link.thumbnail = thumbnail
        if is_visible == 2 or is_visible == 3:
            update_link.summary = summary
        update_link.sharable = update_link.sharable
        update_link.is_visible = is_visible
        update_link.save()
        self.update_linktag(update_link, link_tags)
        self.update_linklabel(update_link, link_labels, user)
        return True
    '''
    [method] = POST
    입력값으로 link 생성한 뒤, DB에 저장
    tag가 입력됐다면 tag저장 후, link와 연결
    '''
    def create(self, request):
        print("link create")

        # 1. user가 유효한지 확인 
        user = request.user
        print(user)
        valid, msg = isvalid_user(user)
        print("create || update")
        
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK) 


        l_id = request.data.get('l_id', None)
        remove = request.data.get('del', None)

        if remove != None:
            #delete
            Link.objects.get(id=l_id).delete()
        elif l_id != None:
            valid, msg = isvalid_link(l_id)
            if not valid:
                print(msg)
                return Response(status=status.HTTP_200_OK)
            
            title = request.data.get('title',None)
            thumbnail = request.data.get('thumbnail',None)
            summary = request.data.get('summary',None)
            is_visible = request.data.get('is_visible', None)

            print(title+" "+thumbnail+" "+summary)
            # if sharable != None:
            #     sharable = int(sharable)
            
            link_tags = request.data.get('tags', None)
            link_labels = request.data.get('labels', None)
            isok = self.link_update(l_id, user, title, thumbnail, summary, is_visible, link_tags,link_labels)

            if not isok:
                print("can't update")
        else:
            url = request.data.get('url', None)
            is_visible = request.get('is_visible', 3)

            if Link.objects.filter(Q(user=user)&Q(url=url)).count() > 0:
                print("user가 이미 등록한 URL")
                return Response(status=status.HTTP_200_OK)
            
            isok = self.link_create(user, url, is_visible)
            if not isok:
                print("유효하지 않는 URL")

        # if l_id == None and del == None:
        #     url = request.data.get('url', None)
        #     is_visible = request.get('is_visible', 3)

        #     if Link.objects.filter(Q(user=user)&Q(url=url)).count() > 0:
        #         print("user가 이미 등록한 URL")
        #         return Response(status=status.HTTP_200_OK)
            
        #     isok = self.link_create(user, url, is_visible)
        #     if not isok:
        #         print("유효하지 않는 URL")
        # else:
        #     valid, msg = isvalid_link(l_id)
        #     if not valid:
        #         print(msg)
        #         return Response(status=status.HTTP_200_OK)
            
        #     title = request.data.get('title',None)
        #     thumbnail = request.data.get('thumbnail',None)
        #     summary = request.data.get('summary',None)
        #     is_visible = request.data.get('is_visible', None)

        #     print(title+" "+thumbnail+" "+summary)
        #     # if sharable != None:
        #     #     sharable = int(sharable)
            
        #     link_tags = request.data.get('tags', None)
        #     link_labels = request.data.get('labels', None)
        #     isok = self.link_update(l_id, user, title, thumbnail, summary, is_visible, link_tags,link_labels)

        #     if not isok:
        #         print("can't update")

        return Response(status=status.HTTP_200_OK)
    
    def exlink_create(self, request):
        print("link create")

        # 1. user가 유효한지 확인 
        email = request.data.get('email', None)
        user = get_user_model().objects.get(email=email)
        valid, msg = isvalid_user(user)
        
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK) 

        url = request.data.get('url', None)
        is_visible = request.get('is_visible', 3)

        if Link.objects.filter(Q(user=user)&Q(url=url)).count() > 0:
            print("user가 이미 등록한 URL")
            return Response(status=status.HTTP_200_OK)
        
        isok = self.link_create(user, url, is_visible)
        if not isok:
            print("유효하지 않는 URL")

        return Response(status=status.HTTP_200_OK)

    # PUT
    def update(self, request):
        # 1. user & link 유효성 체크
        # 유효한 link인지 확인
        print("link update")
        l_id = request.data.get('l_id', None)
        valid, msg = isvalid_link(l_id)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK)

        # user가 유효한지 확인
        user = request.user
        valid, msg = isvalid_user(user)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK) 

        # 2. request에서 data 받고 유효성 체크
        # url = request.data.get('url', None)
        title = request.data.get('title',None)
        thumbnail = request.data.get('thumbnail',None)
        summary = request.data.get('summary',None)
        is_visible = request.data.get('is_visible', None)
        sharable = request.data.get('sharable',None)
        if sharable != None:
            sharable = int(sharable)
        # value가 유효한지 확인
        # isvalid_value()

        # 2. link update
        update_link = Link.objects.get(id=l_id)
        # update_link.url = url
        update_link.title = title
        update_link.sharable = sharable
        
        if is_visible == 1 or is_visible == 3:
            update_link.thumbnail = thumbnail
        if is_visible == 2 or is_visible == 3:
            update_link.summary = summary

        update_link.is_visible = is_visible

        # 3. tag update
        link_tags = request.data.get('tags', None)
        self.update_linktag(update_link, link_tags)

        link_labels = request.data.get('labels', None)
        self.update_linklabel(update_link, link_labels, user)
        # self.update_linklabel(update_link, link_labels)

        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request):
        print("성공!!")
        return Response(status=status.HTTP_200_OK)
    
    def destroy(self, request):
        l_id = request.data.get('l_id', None)
        # 유효한 link인지 확인
        valid, msg = isvalid_link(l_id)
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
        valid, msg = isvalid_user(user)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK)

        search_type = request.data.get('type',None)
        print(search_type)
        if search_type != 'tag' and search_type != None and search_type != 'label' and search_type != 'word':
            print("잘못된 입력으로 검색했습니다.")
            return Response(status=status.HTTP_200_OK)
        
        link_list = Link.objects.all().filter(user=user)

        if search_type == None: # ALL
            result = link_list
        elif search_type == 'word': # search word를 포함한 links
            # content_filter = link_list.filter(Q(summary__icontains=word)|Q(title__icontains=word)) if link_list.filter(Q(summary__icontains=word)|Q(title__icontains=word)).count() > 0 else None
            word = request.data.get('word', None)
            if word == None:
                print("검색 단어가 입력되지 않았습니다.")
                return Response(status=status.HTTP_200_OK)
            
            content_filter = link_list.filter(Q(summary__icontains=word)|Q(title__icontains=word))
            tag_filter = Tag.objects.get(name=word).links.all().filter(id=user.id)
            result = content_filter.union(tag_filter, all=False)
        elif search_type == 'tag': # tag를 포함한 links
            result =  Tag.objects.get(name=word).links.all().filter(id=user.id)
        elif search_type == 'label': # label에 포함된 links
            result = Label.objects.get(name=word).links.all().filter(id=user.id)

        serializer = LinkSerializer(result, many=True)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def create(self, request):
        print("Label create")

        label_name = request.data.get('label_name', None)
        user = request.user

        if label_name != None and Label.objects.filter(Q(name=label_name) & Q(user=user)).count() ==  0:
            Label(name=label_name, user=user).save()
        else:
            print("이미 존재하는 label 또는 label 값이 제대로 입력되지 않음")
    
        return Response(status=status.HTTP_200_OK)
    
    def update(self, request):
        print("label update")

        lb_id = request.data.get('lb_id', None)
        valid, msg = isvalid_label(lb_id)
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK) 

        label_name = request.data.get('label_name', None)
        update_label = Link.objects.get(id=lb_id)
        update_label.name = label_name

        return Response(status=status.HTTP_200_OK) 
    
    def list(self, request):
        # 1. user가 유효한지 확인 
        user = request.user
        print(user)
        valid, msg = isvalid_user(user)
        print("here")
        if not valid:
            print(msg)
            return Response(status=status.HTTP_200_OK) 
        ##############################################

        label_list = Label.objects.filter(user=user)
        serializer = LabelSerializer(label_list, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

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
