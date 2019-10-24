from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LinkViewSet

link_list = LinkViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

link_detail = LinkViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('links/', link_list, name='link_list'),
    path('links/<int:pk>/', link_detail, name='link_detail'),
])
