from django.contrib.auth.models import User
from main_events.serializers import user_serializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
# import the pagination settings
from main_events.pagination import ObjectLimitOffsetPagination, ObjectPageNumberPagination
from rest_framework import status


class UserList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer.UserCreateSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer.UserSerializer