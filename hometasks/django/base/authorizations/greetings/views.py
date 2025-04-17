import json

from django.http.response import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from greetings.models import Greetings

@method_decorator(csrf_exempt, name='dispatch')
class GreetingsView(View):
    def get(self, request):
        greetings = Greetings.objects.all()

        serialized_data = [
            {
                'text': greeting.text,
                'text-id': greeting.id,
            }
            for greeting in greetings
        ]
        return JsonResponse({'data': serialized_data})

    def post(self, request):
        data = json.loads(request.body)
        text = data['text']
        greater = Greetings(text=text)
        greater.save()
        return JsonResponse({
            'data': {
                'id': greater.id,
                'text': greater.text,
            }
        })
