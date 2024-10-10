from .models import Log
import traceback

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = None
        log_entry = Log(url=request.build_absolute_uri(), method=request.method)

        try:
            response = self.get_response(request)
            log_entry.status_code = response.status_code
        except Exception as e:
            log_entry.error_message = traceback.format_exc()
            log_entry.status_code = 500  # Treat as server error
        finally:
            log_entry.save()
            return response
