from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() # SELECT * FROM posts
    serializer_class = PostSerializer # INSERT INTO post VALUES


class PostRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() # SELECT * FROM posts WHERE id = 2
    serializer_class = PostSerializer # UPDATE post SET
                                    # DELETE FROM post WHERE id = 2
