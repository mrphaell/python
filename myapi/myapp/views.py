from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView
)
from .models import User
from .serializers import UserSerializer


class UserAll(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelet(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
