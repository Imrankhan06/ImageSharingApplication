from rest_framework import serializers
from django.contrib.auth import get_user_model
from base.models import Post


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for object author info"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_pic')


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post objects"""
    author = AuthorSerializer(read_only=True)
    photo = serializers.ImageField(max_length=None, allow_empty_file=False)
    liked_by_req_user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'photo',
                  'text', 'location', 'posted_on',
                  'number_of_likes', 'liked_by_req_user')

    def get_liked_by_req_user(self, obj):
        user = self.context['request'].user
        return user in obj.likes.all()
