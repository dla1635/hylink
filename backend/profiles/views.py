from rest_framework import viewsets
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import permissions

# from rest_framework.response import Response
# from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    regist_serializer_class = RegisterSerializer
    permission_classes = (permissions.IsAuthenticated,)

    ordering_fields = '__all__'

    def get_serializer_class(self):
        # if self.action == 'post':
        #     if hasattr(self, 'regist_serializer_class'):
        #         return self.regist_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() 
        # 위의 save 코드로 인해 data가 저장됨
        # return Response({
        #     "user": UserSerializer(user,
        #         context=self.get_serializer_context()).data,
        #     "token": AuthToken.objects.create(user)[1]
        # })
        # return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
