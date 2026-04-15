from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def test_post(request):
    return JsonResponse({'message': 'Hello from test_post!'})

@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        num1 = data.get('a', 0)
        num2 = data.get('b', 0)
        result = num1 + num2
        return JsonResponse({'result': result, 'message': 'Математика працює!'})