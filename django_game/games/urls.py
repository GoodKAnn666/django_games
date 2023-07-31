from django.urls import path


from . import views

urlpatterns = [
    path("", views.GamesView.as_view()),
    path("<slug:slug>/", views.GameDetailView.as_view(), name="game_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]