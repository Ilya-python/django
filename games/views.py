from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Games, Category, Developers, Platforms, Raiting
from django.db.models import Q
from .forms import RaitingForm


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
    отвечает за страницу с одной игрой
    :param slug Уникальный слаг игры
    """
    game = get_object_or_404(Games, game_slug=slug)
    star_form = RaitingForm()
    context = {'game': game, 'star_form': star_form}
    game_id = game.pk
    all_stars = Raiting.objects.filter(game_id=game_id)
    count_user_stars = len(all_stars)
    avg_stars = 0
    for star in all_stars:
        avg_stars += star.star.value
    if count_user_stars >0:
        avg_stars = avg_stars / count_user_stars
    else:
        avg_stars = 0
    context['avg_stars'] = str(round(avg_stars, 1))
    context['count_user_stars'] = str(count_user_stars)
    if request.user.username:
        if Raiting.objects.filter(usrname=request.user, game_id=game_id).exists():
            stars = Raiting.objects.get(usrname=request.user, game_id=game_id).star
            context['stars'] = str(stars)
    return render(request, 'games/sing_game.html', context)


def index1(request):
    content = Games.objects.filter(is_pub=True)
    context = {'games': content}
    return render(request, 'games/home.html', context)


def games_filter(request):
    cat_from_form = request.GET.getlist('cat')
    years_from_form = request.GET.getlist('year')
    if len(cat_from_form) != 0 or len(years_from_form) != 0:
        cats = Category.objects.filter(title__in=cat_from_form)
        games_cat = Games.objects.filter(Q(category__in=cats) | Q(year__in=years_from_form)).distinct()
        context = {'games': games_cat, 'mark': 0}
        return render(request, 'games/games.html', context)
    else:
        messages.error(request, 'юбой текст')
        return redirect('all_games')


def games_by_name(request):
    games = Games.objects.filter(title__icontains=request.GET.get("search_name"))
    if len(games) == 0:
        return redirect('sorry')
    return render(request, 'games/games.html', {'games': games})


def sorry_img(request):
    return render(request, 'games/erorcode.html')


def get_category(request, slug):
    """
    отвечает за страницу содной игрой
    :param slug Уникальный слаг игры
    """
    cat = get_object_or_404(Category, cat_slug=slug)
    return render(request, 'games/category.html', {'cat': cat})


def get_platforms(request, plat_id):
    """
    отвечает за страницу содной игрой
    :param slug Уникальный слаг игры
    """
    plat = get_object_or_404(Platforms, pk=plat_id)
    return render(request, 'games/platforms.html', {'plat': plat})


def get_developers(request, slug):
    """
    отвечает за страницу содной игрой
    :param slug Уникальный слаг игры
    """
    dev = get_object_or_404(Developers, dev_slug=slug)
    return render(request, 'games/developers.html', {'dev': dev})


def add_raiting(request):
    form = RaitingForm(request.POST)
    if form.is_valid():
        Raiting.objects.update_or_create(
            usrname=request.user,
            game_id=int(request.POST.get('game')),
            defaults={'star_id': int(request.POST.get('star'))}
        )

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)
