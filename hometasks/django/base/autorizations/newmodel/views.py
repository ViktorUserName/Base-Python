from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import NewModel

class NewModelView(View):
    def get(self, request):
        data = NewModel.objects.all()

        serialized_data = [
            {
                'id': item.id,
                'name': item.name,
            }
            for item in data
        ]

        return JsonResponse({'data': serialized_data})
# Create your views here.
