from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
import csv

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database

            # Write to CSV file
            with open('user_data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([form.cleaned_data['name'], form.cleaned_data['email']])

            return redirect('success')  # Redirect after successful signup
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})

def success(request):
    return render(request, 'success.html')
