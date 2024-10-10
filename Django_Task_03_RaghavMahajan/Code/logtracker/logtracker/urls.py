from django.contrib import admin
from django.urls import path
from logapp.views import log_graph

def home_view(request):
    return HttpResponse("Welcome to the Log Tracker home page.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logs/graph/', log_graph),
    path('', home_view),
]

