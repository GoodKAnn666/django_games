from django.shortcuts import render
from django.views.generic.base import View

from .models import Game

class GamesView(View):
    def get(self, request):
        games = Game.objects.all()
        return render(request, "games/game_list.html", {"game_list": games})