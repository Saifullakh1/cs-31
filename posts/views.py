from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, PostListSerializer, PostCreateSerializer
from users.models import User


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() # SELECT * FROM posts
    serializer_class = PostListSerializer # INSERT INTO post VALUES

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        elif self.request.method == 'POST':
            return PostCreateSerializer


class PostRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() # SELECT * FROM posts WHERE id = 2
    serializer_class = PostSerializer # UPDATE post SET
                                    # DELETE FROM post WHERE id = 2


class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        post = request.data['post']
        user = request.data['user']
        post_obj = Post.objects.get(id=post)
        user_obj = User.objects.get(id=user)
        like = Like.objects.filter(post=post_obj, user=user_obj).first()
        if like:
            like.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
        else:
            Like.objects.create(user=user_obj, post=post_obj)
            return Response({"message": "Created"}, status=status.HTTP_201_CREATED)
