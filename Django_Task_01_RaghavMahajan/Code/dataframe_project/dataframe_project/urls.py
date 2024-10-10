from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include('data_app.urls')),
    path('', lambda request: redirect('upload_dataframe'))  # Redirect root URL to upload view
]
