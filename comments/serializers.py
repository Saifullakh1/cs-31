from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentForPostSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')

    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'text', 'created_at']