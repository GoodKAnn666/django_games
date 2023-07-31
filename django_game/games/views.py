from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Game
from .forms import ReviewForm

class GamesView(ListView):
    model = Game
    queryset = Game.objects.filter(draft=False)
    template_name = "games/game_list.html"


class GameDetailView(DetailView):
    model = Game
    slug_field = "url"

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        game = Game.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.game = game
            form.save()
        return redirect(game.get_absolute_url())