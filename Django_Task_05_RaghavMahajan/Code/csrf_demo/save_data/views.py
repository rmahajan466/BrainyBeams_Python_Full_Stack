from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

@csrf_exempt
def save_message(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content:
            Message.objects.create(content=content)
            return JsonResponse({"status": "success", "message": "Data saved!"})
        return JsonResponse({"status": "error", "message": "No content provided."})

    return JsonResponse({"status": "error", "message": "Invalid request method."})

def show_form(request):
    return render(request, 'save_data/save_form.html')
