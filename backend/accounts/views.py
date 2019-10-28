# from rest_auth.registration.views import RegisterView
from rest_framework import viewsets 
from .models import MyUser
from .serializers import CustomUserDetailsSerializer

# class CustomRegisterView(RegisterView):
#     queryset = MyUser.objects.all()
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = CustomUserDetailsSerializer
