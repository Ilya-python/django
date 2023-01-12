from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def user_register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_register')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserCreationForm()
    return render(request, 'usercontrols/register.html', {'form':form})


def user_success_register(request):
    return render(request,'usercontrols/success.html')