from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('posts', views.ApiPostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', views.ApiCommentViewSet, basename='comments')
router.register('groups', views.ApiGroupViewSet, basename='groups')
router.register(r'follow', views.ApiFollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
