from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .main import printTest
# Create your views here.


def base(response):
    return render(response, "base.html", {})

def home(request):
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({''})
    return render(request, "home.html")

def chatbox(request):
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({''})
    return render(request, "chatbox.html")

def chat_view(request):
    if request.method == 'POST':
        response_data = printTest()
        return JsonResponse({'response': response_data})
    return render(request, "chatbox.html")

def inventory(request):
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({''})
    return render(request, "inventory.html")

def about(request):
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({''})
    return render(request, "about.html")
