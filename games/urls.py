from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='all_games'),
    path('home/', index1, name='all_games1'),
    path('game/<slug:slug>', get_game, name='single_game'),
    path('filter/',games_filter,name='filter')
]