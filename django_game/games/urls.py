from django.urls import path

from . import views

urlpatterns = [
    path("", views.GamesView.as_view())
]