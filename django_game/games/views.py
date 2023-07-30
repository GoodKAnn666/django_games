from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic.base import View

from .models import Game

class GamesView(ListView):
    model = Game
    queryset = Game.objects.filter(draft=False)
    template_name = "games/game_list.html"


class GameDetailView(DetailView):
    model = Game
    slug_field = "url"