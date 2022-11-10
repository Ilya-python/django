from django.shortcuts import render
from .models import Games, Category


# Create your views here.

def index(request):
    """
    отвечает за гл страницу
    """
    content = Games.objects.filter(is_pub=True)
    context = {'games': content, 'mark': 1}
    return render(request, 'games/games.html', context)


def get_game(request, slug):
    """
    отвечает за страницу содной игрой
    :param slug Уникальный слаг игры
    """
    game = Games.objects.get(game_slug=slug)
    return render(request, 'games/sing_game.html', {'game': game})


def index1(request):
    content = Games.objects.filter(is_pub=True)
    context = {'games': content}
    return render(request, 'games/home.html', context)


def games_filter(request):
    cats = Category.objects.filter(title__in=request.GET.getlist('cat'))
    games_cat = Games.objects.filter(category__in=cats).distinct()
    context = {'games': games_cat, 'mark': 0}
    return render(request, 'games/games.html', context)
