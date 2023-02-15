from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all() #데이터의 범위를 지정한다.
    serializer_class = PostSerializer

# def post_list(request):
#     # 2개 분기
#     pass
#
# def post_detail(request, pk):
#     # request.method # 3개 분기
#     pass