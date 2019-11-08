# Django Post Model_Upgrade

> - 커스터마이징한 User Model로 변경
>
> - 신고 게시글 칼럼 추가 
> - 좋아요 유저 M:N 칼럼 추가 
> - 업데이트 시간 칼럼 추가 
> - 연결된 링크 칼럼 추가 



### posts/models.py

```python
from django.conf import settings
# from django.contrib.auth.models import User 

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # User 모델 부분 변경 
    title = models.CharField(max_length=144)
    contents = models.TextField(blank=True) # 빈칸 가능 
    links = models.ManyToManyField(Link, related_name='link_posts') # 추가 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True) # 좋아요 유저 추가 

```

게시글 신고기능 추가 

```python
class PostReport(models.Model):
    report_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='report_posts', blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="report_list")
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



## Python Shell Plus

>  sql 쿼리문으로 생성한 모델 확인할 때 유용한 Tool 

Django extensions  설치 통해 이용함 

```bash
$ pip lnstall django-extensions 
```

### settings/dev.py

```python
INSTALLED_APPS = (
	```
    'django_extensions',
)
```

실행

```bash
$ python manage.py shell_plus 
```



## Serializers 

> PostReport 모델에 맞는 Serializer 생성 

### posts/serializers.py

포스트 시리얼라이저에 '좋아요 유저들' 추가 

업데이트 및 연결 링크들 추가 

```python
from backend.links.models import Link 
from backend.links.serializers import LinkSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    links = LinkSerializer(read_only=True, many=True) # 추가 
    like_users = UserSerializer(read_only=True, many =True) # 추가 
    
    class Meta:
        model = Post
        fields = (
            *** 
            'links', # 추가 
            'created_at',
            'updated_at', # 추가
            *** 
            'link_users', # 추가 
        )
        read_only_fields = ('created_at', 'updated_at')
```

신고당한 포스트들에 대한 정보를 담을 시리얼라이저 추가 

```python 
class ReportSerializer(serializers.ModelSerializer):
    report_users = UserSerializer(read_only=True, many=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = PostReport
        fields = (
            'id',
            'contents',
            'created_at',
            'post',
            'report_users'
        )
        read_only_fields = ('created_at',)

```



### posts/serializers.py

최종적으로 수정한 serializers.py 파일 

```python
from rest_framework import serializers
from .models import Post 
from .models import PostComment
from .models import PostReport
from backend.links.models import Link 
from backend.links.serializers import LinkSerializer
# from django.contrib.auth.models import User
# from django.conf import settings
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model(),
        fields = ('id', 'email', 'nickname')


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)
    links = LinkSerializer(read_only=True, many=True)
    links_id = serializers.PrimaryKeyRelatedField(queryset=Link.objects.all(), write_only=True, many=True)
    like_users = UserSerializer(read_only=True, many =True)
    like_users_id = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), write_only=True, many=True)
    
    class Meta:
        model = Post
        fields = (
            'pk',
            'title',
            'contents',
            'links',
            'links_id',
            'created_at',
            'updated_at',
            'view_count',
            'like_count',
            'user',
            'like_users',
            'like_users_id'
        )
        read_only_fields = ('pk', 'created_at', 'updated_at',)


    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['user']


    def create(self, validated_data):
        links = validated_data.pop('links_id')
        posts = Post.objects.create(**validated_data)
        for lk in links:
            posts.links.add(lk)
        return posts 


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)
    post = PostSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)


    class Meta:
        model = PostComment
        fields = (
            'pk',
            'contents',
            'created_at',
            'updated_at',
            'user',
            'post',
            'post_id'
        )
        read_only_fields =('pk', 'created_at', 'updated_at',)


    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(CommentSerializer, self).get_validation_exclusions()

        return exclusions + ['user']


    def create(self, validated_data):
        post = validated_data.pop('post_id')
        comments = PostComment.objects.create(post=post, **validated_data)
        return comments



class ReportSerializer(serializers.ModelSerializer):
    report_users = UserSerializer(read_only=True, many=True)
    report_users_id = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), write_only=True, many=True)
    post = PostSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)
    

    class Meta:
        model = PostReport
        fields = (
            'pk',
            'contents',
            'created_at',
            'updated_at',
            'post',
            'post_id',
            'report_users',
            'report_users_id'
        )
        read_only_fields = ('pk', 'created_at', 'updated_at',)

    
    
    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ReportSerializer, self).get_validation_exclusions()

        return exclusions


    def create(self, validated_data):
        report_users = validated_data.pop('report_users_id')
        post = validated_data.pop('post_id')
        reports = PostReport.objects.create(post=post, **validated_data)
        for ru in report_users:
            reports.report_users.add(ru)
        return reports

```



## Viewset 설정

### posts/views.py

```python
from rest_framework import viewsets
from .models import Post, PostComment, PostReport
from .serializers import PostSerializer, CommentSerializer, ReportSerializer
from rest_framework import permissions


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = PostReport.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()
```

