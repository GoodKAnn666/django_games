from django.contrib import admin
from .models import Category, Developer, Genre, Game, GameShorts, TopReating, Rating, Reviews

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    list_display_links = ("name",)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category",)
    search_fields = ("title", "category__name")
    list_editable = ("draft",)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("game", "name", "email", "text")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(GameShorts)
class GameShortsAdmin(admin.ModelAdmin):
    list_display = ("title", "games")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("ip", "game")


# admin.site.register(Category)
# admin.site.register(Developer)
# admin.site.register(Genre)
# admin.site.register(Game)
# admin.site.register(GameShorts)
# admin.site.register(Rating)
# admin.site.register(Reviews)
