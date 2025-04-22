from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from django.utils import timezone

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(deleted_at__isnull=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_soft_delete(self, instance):
        instance.deleted_at = timezone.now()
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Post deleted'},status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def all_posts(self, request):
        try:
            posts = Post.objects.all()  
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def soft_delete(self, request, pk=None):
        try:
            post = self.get_object()
            self.perform_soft_delete(post)
            return Response({'message': 'Post marked as deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)},status=status.HTTP_400_BAD_REQUEST)
