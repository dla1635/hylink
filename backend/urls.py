"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from .api.views import index_view, MessageViewSet
from .posts.views import PostViewSet, CommentViewSet, ReportViewSet
from .links.views import LinkViewSet, LinksViewSet, LabelViewSet
from .sharing.views import ShareViewSet 
from .profiles.views import UserViewSet

# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('linklist', LinksViewSet)
router.register('link', LinkViewSet)
router.register('label', LabelViewSet)
router.register('share', ShareViewSet)
router.register('reports', ReportViewSet)
router.register('users', UserViewSet)


urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

    path('auth/token/', obtain_jwt_token, name='api_token'),

    path('auth/', include('rest_auth.urls')),

    url(r'^auth/registration/', include('rest_auth.registration.urls')),

    url(r'^auth/accounts/', include('allauth.urls')),

    # path('api/auth/verify', verify_jwt_token),

    # path('api/auth/refresh', refresh_jwt_token),

    url(r'^.*$',  index_view, name='index')

]
