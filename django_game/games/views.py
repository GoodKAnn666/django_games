from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View

from .models import Game, Category, Developer, Genre, Rating
from .forms import ReviewForm, RatingForm


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Game.objects.filter(draft=False).values("year")


class GamesView(GenreYear, ListView):
    model = Game
    queryset = Game.objects.filter(draft=False)
    template_name = "games/game_list.html"
    paginate_by = 2


class GameDetailView(GenreYear, DetailView):
    model = Game
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["top_form"] = RatingForm()
        return context


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
    paginate_by = 1

    def get_queryset(self):
        if 'genre' in self.request.GET and 'year' in self.request.GET:
            print('if genre and year')
            queryset = Game.objects.filter(
                Q(year__in=self.request.GET.getlist("year")), Q(genres__in=self.request.GET.getlist("genre"))
            )
        else:
            print('else')
            queryset = Game.objects.filter(
                Q(year__in=self.request.GET.getlist("year")) | Q(genres__in=self.request.GET.getlist("genre"))
            ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context


class AddTopRating(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                game_id=int(request.POST.get("game")),
                defaults={'top_id': int(request.POST.get("top"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(ListView):
    """Поиск игр через кнопку 'поиск' """
    paginate_by = 3

    def get_queryset(self):
        return Game.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
