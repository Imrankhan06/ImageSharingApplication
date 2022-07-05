from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post import views

router = DefaultRouter()
router.register('', views.PostViewSet)

app_name = 'post'

urlpatterns = [
    path('feeds/', views.UserFeedView.as_view(), name='feeds'),
    path('', include(router.urls)),
    path('like/<slug:post_id>/', views.LikeView.as_view(), name='like'),
    path('<slug:post_id>/get-likers/', views.GetLikersView.as_view(), name='get-likers'),
]
