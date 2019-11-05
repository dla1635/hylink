from django.contrib import admin
from django.urls import path
from .views import ShareViewSet

share = ShareViewSet.as_view({
    'post' : 'create'
})

sharelist = ShareViewSet.as_view({
    'get' : 'list'
})

urlpatterns = [
    path('share/', share, name='share'),
    path('share/<int:pk>/', sharelist, name='sharelist')
]
