import datetime as dt

from posts.models import Comment, Follow, Group, Post
from rest_framework import permissions, viewsets

from .permissions import PermissionReadOrCreate
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PermissionReadOrCreate, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, pub_date=dt.date.today())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (PermissionReadOrCreate, )

    def get_post_id(self):
        post_id = self.kwargs.get('post_id')
        return post_id

    def get_queryset(self):
        permission_queryset = Comment.objects.filter(
            post_id=self.get_post_id()
        )
        return permission_queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            created=dt.datetime.now(),
            post_id=self.get_post_id()
        )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(
            user=self.request.user
        )
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
