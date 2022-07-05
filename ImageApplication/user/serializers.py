from rest_framework import serializers
from django.contrib.auth import get_user_model
from base.models import Post
from django.core.paginator import Paginator
from rest_framework.settings import api_settings


class UserPostsSerializer(serializers.ModelSerializer):
    """Serializer for viewing a user profile"""

    class Meta:
        model = Post
        fields = ('id', 'photo', 'text', 'location', 'number_of_likes', 'posted_on')


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for registering a user"""
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'fullname', 'username', 'password', 'profile_pic', 'bio')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserInfoSerializer(serializers.ModelSerializer):
    """Serializer for user information"""
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password', 'fullname', 'profile_pic', 'bio')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for viewing a user posts"""
    number_of_posts = serializers.SerializerMethodField()
    followed_by_req_user = serializers.SerializerMethodField()
    user_posts = serializers.SerializerMethodField('paginated_user_posts')

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'fullname',
                  'bio', 'profile_pic', 'number_of_followers',
                  'number_of_following', 'number_of_posts',
                  'user_posts', 'followed_by_req_user')

    def get_number_of_posts(self, obj):
        return Post.objects.filter(author=obj).count()

    def paginated_user_posts(self, obj):
        page_size = api_settings.PAGE_SIZE
        paginator = Paginator(obj.user_posts.all(), page_size)
        page = self.context['request'].query_params.get('page') or 1

        user_posts = paginator.page(page)
        serializer = UserPostsSerializer(user_posts, many=True)

        return serializer.data

    def get_followed_by_req_user(self, obj):
        user = self.context['request'].user
        return user in obj.followers.all()


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for listing all followers"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_pic')


class AllUsersInfoSerializers(serializers.ModelSerializer):
    """Serializer for listing all users"""
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'fullname',
                  'bio', 'profile_pic', 'number_of_followers',
                  'number_of_following', 'number_of_posts',
                  'user_posts', 'followed_by_req_user')
