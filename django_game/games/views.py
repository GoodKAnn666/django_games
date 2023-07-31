from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic.base import View

from .models import Game, Category, Developer, Genre
from .forms import ReviewForm



class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Game.objects.filter(draft=False).values("year")

class GamesView(GenreYear, ListView):
    model = Game
    queryset = Game.objects.filter(draft=False)
    template_name = "games/game_list.html"



class GameDetailView(GenreYear, DetailView):
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


class DeveloperView(GenreYear, DetailView):
    model = Developer
    template_name = "games/developer.html"
    slug_field = "name"


class FilterGamesView(GenreYear, ListView):
    def get_queryset(self):
        queryset = Game.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset