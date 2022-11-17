from django import template
from games.models import Category, Games

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('tags/last_games.html')
def get_last_games():
    last_games = Games.objects.all().order_by('id')[:3]
    return {'last_games':last_games}

@register.simple_tag()
def get_years():
    games = Games.objects.filter(is_pub=True)
    years = []
    for game in games:
        y = game.year
        if y not in years:
            years.append(y)
    return years
