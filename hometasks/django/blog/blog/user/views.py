import json
from django.contrib.auth import get_user_model, authenticate
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken

CustomUser = get_user_model()

def jwt_required(func):
    def wrapper(self, request, *args, **kwargs):  # Добавляем self
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return JsonResponse({'error': 'Token is missing'}, status=401)
        try:
            access_token = token.split(' ')[1]
            AccessToken(access_token)
        except Exception as e:
            return JsonResponse({"error": f"Token is invalid: {str(e)}"}, status=401)
        return func(self, request, *args, **kwargs)  # Добавляем self
    return wrapper


@method_decorator(csrf_exempt, name='dispatch')
class RegisterUserView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        if 'username' not in data or 'password' not in data or 'email' not in data:
            return JsonResponse({'error': 'Missing username and password.'}, status=400)

        user = CustomUser(
            username=data['username'],
            email=data['email'],
            password=make_password(data['password']),
            role= data.get('role', 'Author'),
        )
        user.save()

        return JsonResponse({'user': f'create sucses {user.id}'}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class LoginUserView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        if 'username' not in data or 'password' not in data or 'email' not in data:
            return JsonResponse({'error': 'Missing username and password.'}, status=400)

        user = authenticate(username=data['username'], password=data['password'])

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return JsonResponse({'token': access_token}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

class CurrentUserView(View):
    @jwt_required
    def get(self, request, *args, **kwargs):
        user = request.user
        return JsonResponse({
            'user': f'current user is {user.id}',
            'role': user.role,
            'email': user.email,
        }, status=200)
