from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    login_serializer_class = LoginSerializer
    regist_serializer_class = RegisterSerializer
    permission_classes = (permissions.IsAuthenticated,)

    ordering_fields = '__all__'

    # def get_serializer_class(self):
    #     if self.action == 'post':
    #         if hasattr(self, 'regist_serializer_class'):
    #             return self.regist_serializer_class
    #     return super().get_serializer_class()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save() 
    #     # 위의 save 코드로 인해 data가 저장됨
    #     return Response({
    #         "user": UserSerializer(user,
    #             context=self.get_serializer_context()).data,
    #         "token": AuthToken.objects.create(user)[1]
    #     })