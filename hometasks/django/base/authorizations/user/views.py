from django.shortcuts import render
from django.contrib.auth.models import AbstractBaseUser

from django.views import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate
from  django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import jwt
import datetime
from django.conf import settings
from functools import wraps



User = get_user_model()


def jwt_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Authorization header missing or invalid'}, status=401)

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['id'])
            request.user = user  # 👈 теперь во view-функции можно обращаться к request.user
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapped_view

def generate_jwt_token(user):
    payload = {
        'id': user.id,
        'username': user.username,
        'exp': datetime.datetime.now() + datetime.timedelta(days=1),
        'iat': datetime.datetime.now(),
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token if isinstance(token, str) else token.decode('utf-8')

@method_decorator(csrf_exempt, name='dispatch')
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
            return JsonResponse({'new_user' : {'id': user.id, 'username': user.username}}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class TokenView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({'error': 'invalid credentials'}, status=401)

        token = generate_jwt_token(user)
        print(settings.SECRET_KEY)
        print(f"RAW TOKEN: {token} | TYPE: {type(token)}")

        return JsonResponse({'token': token}, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request):
        auth = request.headers.get('Authorization')
        if not auth or not auth.startswith('Bearer '):
            return JsonResponse({'message': 'hi guiest'}, status=200)
        token_str = auth.split()[1]
        # print(f"AUTH HEADER: {auth}")
        # print(f"TOKEN STR: {token_str}")
        # print(f"SECRET_KEY: {settings.SECRET_KEY}")

        try:
            # payload = jwt.decode(token_str, settings.SECRET_KEY, algorithms=['HS256'])
            payload = jwt.decode(token_str, options={"verify_signature": False})
            user = User.objects.get(id=payload['id'])
            if user.role == 'author':
                return JsonResponse({'message': f'hello {user.username}!'}, status=200)
            else:
                return JsonResponse({'message': f'hello {user.username} you are not author!'}, status=401)
        except jwt.ExpiredSignatureError:
            print("JWT ERROR: expired")
            return JsonResponse({'message': 'token expired'}, status=401)
        except jwt.InvalidTokenError:
            print("JWT ERROR: invalid")
            return JsonResponse({'message': 'invalid token'}, status=401)
        except User.DoesNotExist:
            print("JWT ERROR: user not found")
            return JsonResponse({'message': 'user does not exist'}, status=401)
        except Exception as e:
            print(f"UNEXPECTED JWT ERROR: {e}")
            return JsonResponse({'message': str(e)}, status=500)
