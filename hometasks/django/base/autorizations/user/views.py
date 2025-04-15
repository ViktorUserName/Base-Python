from django.shortcuts import render
from django.contrib.auth.models import AbstractBaseUser

from django.views import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate
from  django.contrib.auth.hashers import make_password
import json

from autorizations.user.models import Token

User = get_user_model()

class RegisterView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'error': 'username and password are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'username already exists'}, status=400)\

        try:
            user = User.objects.create(
                username=username,
                password=make_password(password),
            )
            return JsonResponse({'user': user}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


class TokenView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user: AbstractBaseUser | None = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({'error': 'invalid credentials'}, status=401)

        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key}, status=200)

class MainView(View):
    def get(self, request):
        auth = request.headers.get('Authorization')
        if not auth or not auth.startswith('Token '):
            return JsonResponse({'message': 'hi guiest'})

        token_key = auth.split()[1]
        try:
            token = Token.objects.get(key=token_key)
            return JsonResponse({'message': f'hi {token.user.username}'}, status=200)
        except Token.DoesNotExist:
            return JsonResponse({'message': 'no such token'}, status=401)
