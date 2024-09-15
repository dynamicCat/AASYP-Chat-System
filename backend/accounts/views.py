from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, require_POST
from .forms import RegisterForm
import json

@require_POST
def update_timezone(request):
    data = json.loads(request.body)
    timezone = data.get('timeZone')

    print(f"Received timezone: {timezone}")  

    if timezone:
        request.user.timezone = timezone
        request.user.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'fail'}, status=400)

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = RegisterForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'message': 'Registration successful!'}, status=200)
        else:
            return JsonResponse({'message': 'Registration failed', 'errors': form.errors}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful!'}, status=200)
        else:
            return JsonResponse({'message': 'Login failed, invalid credentials'}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)
