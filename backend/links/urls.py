from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LinkViewSet, LinksViewSet, LabelViewSet

linklist = LinksViewSet.as_view({
    'get': 'list'
})

link = LinkViewSet.as_view({
    'post': 'create',
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

label = LabelViewSet.as_view({
    'post' : 'create',
    'put' : 'update',
    'get' : 'list'
})


urlpatterns = format_suffix_patterns([
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('linklist/', linklist, name='linklist'),
    path('link/$', link, name='link'),
    path('label/$', label, name='label')
])
