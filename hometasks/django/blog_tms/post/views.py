import json
from django.http import JsonResponse
from django.views import View
from post.models import Post
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class PostView(View):
    def get(self, request):
        posts = Post.objects.all()

        data_serialized = [
            {
                "title": post.title,
                "content": post.content
            } for post in posts
        ]
        return JsonResponse({"posts": data_serialized}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        if not title or not content:
            return JsonResponse({'error': 'title and content are required'}, status=400)

        new_post = Post(title=title, content=content)
        new_post.save()

        return JsonResponse({
            'message': 'Post created successfully',
            'post': {
                'id': new_post.id,
                'title': new_post.title,
                'content': new_post.content,
            }
        }, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class PostDetailView(View):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            serialized_post = {'post_id': post.id,'title': post.title, 'content': post.content}
            return JsonResponse(serialized_post, status=200)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)

    def put(self, request, post_id):
        try:
            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')

            post = Post.objects.get(id=post_id)
            post.title = title
            post.content = content
            post.save()
            return JsonResponse({'message': 'Post updated successfully'}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return JsonResponse({'message': 'Post deleted successfully'}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)