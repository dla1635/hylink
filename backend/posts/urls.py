from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewSet
from .views import CommentViewSet
from .views import ReportViewSet

post_list = PostViewSet.as_view({
    'post': 'create',
    'get': 'list'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
comment_list = CommentViewSet.as_view({
    'post': 'create',
    'get':'list'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
report_list = ReportViewSet.as_view({
    'post': 'create',
    'get':'list'
})

urlpatterns = format_suffix_patterns([
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('comments/', comment_list, name='comment_list'),
    path('comments/<int:pk>/', comment_detail, name='comment_detail'),
    path('reports/<int:pk>/', report_list, name='report_list'),
])
