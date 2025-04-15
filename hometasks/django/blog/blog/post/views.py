import json

from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        data = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'likes': post.likes,
                'created': post.created,
                'updated': post.updated,
                'user': post.user.username
            } for post in posts
        ]
        return JsonResponse({'posts': data}, status=200)

    def post(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        print(request.user)
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)

        if request.user.role not in ['Admin', 'Author']:
            return JsonResponse({'error': 'Permission denied'}, status=403)

        try:
            data = json.loads(request.body)

            if 'title' not in data or 'content' not in data:
                return JsonResponse({'error': 'Both title and content are required'}, status=400)

            post = Post(
                title=data['title'],
                content=data['content'],
                user=request.user
            )
            post.save()

            return JsonResponse({
                'message': 'Post created successfully',
                'post': {
                    'id': post.id,
                    'title': post.title,
                    'content': post.content,
                    'user': post.user.username,
                    'created': post.created
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
