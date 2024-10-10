from django.db import models

class Log(models.Model):
    url = models.URLField()
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    error_message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.method} {self.url} - {self.status_code}'
