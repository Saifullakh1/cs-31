from rest_framework import serializers
from .models import Post, Like
from comments.serializers import CommentForPostSerializer


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'user_name']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    user_name = serializers.CharField(source='user.name')
    post_comments = CommentForPostSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'user_name', 'image', 'likes', 'post_comments']

    def get_likes(self, obj):
        likes = Like.objects.filter(post=obj)
        return len(likes)
