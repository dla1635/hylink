from rest_framework import viewsets
from .models import Post, PostComment, PostReport
from .serializers import PostSerializer, CommentSerializer, ReportSerializer
from rest_framework import permissions
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # POST
    def create(self, request):
        user = request.user
        title = request.data.get('title', None)
        contents = request.data.get('contents', None)
        links = request.data.get('links', None)

        post = Post(user=user, title=title, contents=contents, view_count=0,like_count=0)
        post.save()

        for link in links:
            post_link = Link.objects.get(id=link)
            post.links.add(post_link)

        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request):
        user = request.user
        post_id = request.data.GET('p_id', None)
        post = Post.objects.get(id=post_id, user=user)
        serializer = PostSerializer(post, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request):
        user = request.user
        p_id = request.data.get('p_id', None)
        title = request.data.get('title', None)
        contents = request.data.get('contents', None)
        links = request.data.get('links', None)

        return Response(status=status.HTTP_200_OK)


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
