from django.urls import path

from . import views


urlpatterns = [
    path("", views.GamesView.as_view()),
    path("filter/", views.FilterGamesView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("add_rating/", views.AddTopRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.GameDetailView.as_view(), name="game_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("developer/<str:slug>/", views.DeveloperView.as_view(), name="developer_detail"),
]
