from django.shortcuts import render
from .models import Games
# Create your views here.

def index(request):
    content = Games.objects.filter(is_pub=True)
    context = {'games':content, 'mark':1}
    return render(request, 'games/games.html', context)

def get_game(request, slug):
    game = Games.objects.get(game_slug=slug)
    return render(request, 'games/sing_game.html', {'game':game})

def index1(request):
    content = Games.objects.filter(is_pub=True)
    context = {'games':content}
    return render(request, 'games/home.html', context)