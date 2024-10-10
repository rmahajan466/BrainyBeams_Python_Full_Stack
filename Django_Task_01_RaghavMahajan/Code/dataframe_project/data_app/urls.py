# data_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_dataframe, name='upload_dataframe'),
    path('show_data/', views.show_data, name='show_data'),
]
