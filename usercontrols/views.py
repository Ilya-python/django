from django.shortcuts import render, redirect
from .forms import UserRedirecterForms, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import CommentForm
from games.models import Games

# Create your views here.


def user_register(request):
    if request.method=='POST':
        form = UserRedirecterForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_register')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRedirecterForms()
    return render(request, 'usercontrols/register.html', {'form':form})


def user_success_register(request):
    return render(request,'usercontrols/success.html')

def user_login(request):
    if request.method=='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('all_games')
        else:
            messages.error(request, "Ошибка авторизации")
    else:
        form = UserLoginForm()
    return render(request, 'usercontrols/login.html', {'forms':form})


def user_success_out(request):
    logout(request)
    return render(request,'usercontrols/logout.html')


def add_comment(request, pk):
    form = CommentForm(request.POST)
    if request.method == 'POST':
        form = form.save(commit=False)
        if request.POST.get('parent', None):
            form.parent_id = int(request.POST.get('parent'))
        form.name = request.user
        form.game_id = pk
        form.save()
        game = Games.objects.get(pk=pk)
    return redirect(game.get_absolute_url())