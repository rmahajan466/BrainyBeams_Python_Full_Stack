from django.urls import path
from . import views

urlpatterns = [
    path('save-message/', views.save_message, name='save_message'),
    path('submit-form/', views.show_form, name='show_form'),
]
