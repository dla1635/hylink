from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import CurrentUserSerializer
from rest_framework import viewsets


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer