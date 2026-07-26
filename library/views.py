from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Member
import random
def home(request):
    return render(request, 'library/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            member_id = f"MEM{random.randint(1000, 9999)}"
            Member.objects.create(user=user, member_id=member_id)
            messages.success(request, f'Account created! Your Member ID is {member_id}. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})