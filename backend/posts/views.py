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
        serializer.save(user=self.request.user, post=self.request.post)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = PostReport.objects.all()
    serializer_class = ReportSerializer