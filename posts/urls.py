from django.urls import path
from .views import PostAPIView, PostRetrieveAPIView, LikeCreateAPIView


urlpatterns = [
    path('', PostAPIView.as_view(), name='list'),
    path('<int:pk>', PostRetrieveAPIView.as_view(), name='retrieve'),
    path('like', LikeCreateAPIView.as_view(), name='create-like')
]
