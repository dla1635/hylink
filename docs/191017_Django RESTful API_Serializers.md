# Django RESTful API_Serializers

> Serializers를 이용한 Post 모델 구현 



현재 Hylink 프로젝트의 디렉터리 구조 

```
backend
├── api
│   ├── migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── settings
├── __init__.py
├── settings.py
├── urls.py
└── wsgi.py
manage.py
db.sqlite3
```



## Posts App 생성 

참고한 포스트와 달리 이미 Vue와 연동한 api app이 샘플로 생성되어 있기 때문에 구분을 위해 새로운 posts app을 만들어 보겠습니다. 



```bash
$ python manage.py startapp posts
```



## Models 생성

### Post DB

![캡처](https://lab.ssafy.com/s1-final/hylink/uploads/55b156e2814f53e0581ec5bc4ab6051c/%EC%BA%A1%EC%B2%98.PNG)



기존 장고 방식으로 현재 Post Model 구성했을 때 코드 

#### post/models.py

```python
from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
    user = model.ForeignKey(User, on_delete=models.CASCADE) # CASCADE = 삭제시 foreignkey를 포함하는 모델 인스턴스도 삭제
    title = model.CharField(max_length=144)
    contents = model.TextField(blank=True) # 빈칸 가능 
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = model.IntegerField(default=0)
    like_count = model.IntegerField(default=0)
    
    # admin 페이지에서 보여줄 내용 
    def __str__(self):
        return '[{}] {}'.format(self.user.username, self.title)
```



> Model 코드를 수정했을 경우, sqlite에 테이블을 새로 생성시키기 위해 반드시 migrate을 다시 해주어야 합니다

```bash
$ python manage.py makemigrations <app이름>
$ python manage.py migrate <app이름>
```



## Serializers 생성

### Serializer?

기존 Django를 이용한 Django ORM의 Queryset는 Django template로 넘어가면서 HTML로 렌더링되고, Response로 보내집니다. 

Vue와 연결도 손쉽게 하면서 RESTful API로 만들기 위해서는 JSON 데이터를 보내야하는데, 그러면 HTML로 렌더링 되는 Django Template를 사용할 수 없습니다. 그래서 Queryset를 JSON으로 매핑하는 과정을 Serializer가 도와주는 역할을 담당합니다. 



![django_serializer](https://miro.medium.com/max/2048/1*AjXUSAQ5WPHi2lvfRKD08g.jpeg)



Django REST framework가 제공하는 `ModelSerializer`를 이용해 api에 serializers.py 파일을 생성해서 새로운 코드를 작성해보겠습니다. 



### post/serializers.py

```python
from rest_framework import serializers
from .models import Post 
from django.contrib.auth.models import User

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializer.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'contents',
            'created_at',
            'view_count',
            'like_count'
        )
        read_only_fields = ('created_at',)
```



## Views 생성

Viewset를 이용해 Model 하나를 컨트롤하는 CRUD를 구현합니다.



### post/views.py

```python
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated)
    def perform_create(self, seriallizer):
        serializer.save(user=self.request.user)
```



### post/urls.py

```python
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})
post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
])
```



루트 URL에 매핑시켜줍니다. 

### api/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet
from .post.views import PostViewSet # 추가 

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('post', PostViewSet) # 추가

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]

```





## 참고문헌

- [장고로 간단한 블로그 만들기]([https://medium.com/wasd/django%EB%A1%9C-%EA%B0%84%EB%8B%A8%ED%95%9C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-%EA%B0%9C%EC%9A%94-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%84%B1-83d03ec74395](https://medium.com/wasd/django로-간단한-블로그-만들기-1-개요-프로젝트-구성-83d03ec74395))

- [RESTful API in Django](https://medium.com/wasd/restful-api-in-django-16fc3fb1a238)