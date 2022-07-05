from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.RegisterUserView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('home/', views.ManageUserView.as_view(), name='home'),
    path('<slug:username>/', views.UserProfileView.as_view(), name='user-profile'),
    path('<slug:username>/follow/', views.FollowUserView.as_view(), name='follow-user'),
    path('<slug:username>/get-followers/', views.GetFollowersView.as_view(), name='get-followers'),
    path('<slug:username>/get-following/', views.GetFollowingView.as_view(), name='get-following'),
    path('<slug:username>/allusers/', views.AllUserInfoView.as_view(), name='allusers'),
]
