from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from .permissions import IsOwnerPermission

from posts.models import User, Post, Group, Comment, Follow
from .serializers import (ApiPostSerializer, ApiCommentSerializer,
                          ApiFollowSerializer, ApiGroupSerializer)


class ApiPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ApiPostSerializer
    permission_classes = (IsOwnerPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ApiGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = ApiGroupSerializer
    permission_classes = (IsOwnerPermission,)


class ApiFollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = ApiFollowSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('user__username', 'following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)


class ApiCommentViewSet(viewsets.ModelViewSet):
    serializer_class = ApiCommentSerializer
    permission_classes = (IsOwnerPermission,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)
