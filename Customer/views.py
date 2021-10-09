from django.shortcuts import redirect, render
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def sign_in(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'Home.html', context)

def login(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'Home.html', context)