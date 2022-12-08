from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='all_games'),
    path('home/', index1, name='all_games1'),
    path('game/<slug:slug>', get_game, name='single_game'),
    path('filter/', games_filter, name='filter'),
    path('search/', games_by_name, name='search'),
    path('sorry/', sorry_img, name='sorry'),
    path('plat/<int:plat_id>', get_platforms, name='plat'),
    path('category/<slug:slug>', get_category, name='cat'),
    path('developers/<slug:slug>', get_developers, name='dev')
]
