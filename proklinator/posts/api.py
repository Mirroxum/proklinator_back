from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer

class PostsAPI(ListCreateAPIView):
    class PostsListPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'

    queryset = Post.objects.filter(is_active = True)
    serializer_class = PostSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created_at', 'updated_at', 'id')
    ordering = '-created_at'
    pagination_class = PostsListPagination


class LikeAPI(UpdateAPIView):
    queryset = Post.objects.all()

    def patch(self, request, *args, **kwargs):
        post = get_object_or_404(self.get_queryset(), id=request.query_params.get('id'))
        post.likes += 1
        post.save()
        return Response({'likes': post.likes})
    