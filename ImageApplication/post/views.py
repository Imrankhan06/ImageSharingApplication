from rest_framework import permissions, viewsets, generics, status
from .serializers import PostSerializer, AuthorSerializer
from .permissions import IsOwnerOrReadOnly, IsOwnerOrPostOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from base.pagination import FollowersLikersPagination
from base.models import Post


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        queryset = Post.objects.all().filter(author__in=following_users)
        return queryset


class LikeView(APIView):
    """Toggle like"""

    def get(self, post_id=None):
        post = Post.objects.get(pk=post_id)
        user = self.request.user
        like = None
        if user.is_authenticated:
            if user in post.likes.all():
                like = False
                post.likes.remove(user)
            else:
                like = True
                post.likes.add(user)
        data = {
            'like': like
        }
        return Response(data)


class GetLikersView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    pagination_class = FollowersLikersPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        queryset = Post.objects.get(
            pk=post_id).likes.all()
        return queryset