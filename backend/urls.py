"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet
from .posts.views import PostViewSet, CommentViewSet, ReportViewSet
from .links.views import LinkViewSet, LinksViewSet 
from .accounts.views import UserViewSet

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('linklist', LinksViewSet)
router.register('link', LinkViewSet)
router.register('reports', ReportViewSet)
router.register('users', UserViewSet)


urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    # login, registration 등 path 설정 
    path('api/users/rest-auth/', include('rest_auth.urls')),
    # 토큰 발급 및 재발급 페이지 설정 
    path('api/users/rest-auth/obtain_token/', obtain_jwt_token, name="obtain-jwt" ),
    path('api/users/rest-auth/refresh_token/', refresh_jwt_token, name="refresh-jwt"),

    path('api/users/rest-auth/registration/', include('rest_auth.registration.urls')),

]
