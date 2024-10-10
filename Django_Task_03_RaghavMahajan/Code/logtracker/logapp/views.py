import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from .models import Log

def log_graph(request):
    logs = Log.objects.all()
    success_count = logs.filter(status_code__lt=400).count()
    error_count = logs.filter(status_code__gte=400).count()

    fig, ax = plt.subplots()
    ax.bar(['Success', 'Errors'], [success_count, error_count])
    ax.set_title('Success vs Errors in Logs')
    ax.set_ylabel('Number of Requests')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return HttpResponse(buffer, content_type='image/png')
