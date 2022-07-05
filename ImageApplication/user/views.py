from rest_framework import generics, permissions
from .serializers import RegisterUserSerializer, UserInfoSerializer, UserProfileSerializer, FollowSerializer, \
    AllUsersInfoSerializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from base.pagination import FollowersLikersPagination


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user


class UserProfileView(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny,)


class FollowUserView(APIView):

    def get(self, username=None):
        to_user = get_user_model().objects.get(username=username)
        from_user = self.request.user
        follow = None
        if from_user.is_authenticated:
            if from_user != to_user:
                if from_user in to_user.followers.all():
                    follow = False
                    from_user.following.remove(to_user)
                    to_user.followers.remove(from_user)
                else:
                    follow = True
                    from_user.following.add(to_user)
                    to_user.followers.add(from_user)
        data = {
            'follow': follow
        }
        return Response(data)


class GetFollowersView(generics.ListAPIView):
    serializer_class = FollowSerializer
    pagination_class = FollowersLikersPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        username = self.kwargs['username']
        queryset = get_user_model().objects.get(
            username=username).followers.all()
        return queryset


class GetFollowingView(generics.ListAPIView):
    serializer_class = FollowSerializer
    pagination_class = FollowersLikersPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        username = self.kwargs['username']
        queryset = get_user_model().objects.get(
            username=username).following.all()
        return queryset


class AllUserInfoView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny,)
