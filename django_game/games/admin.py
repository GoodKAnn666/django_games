from django.contrib import admin
from .models import Category, Developer, Genre, Game, GameShorts, TopReating, Rating, Reviews

admin.site.register(Category)
admin.site.register(Developer)
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(GameShorts)
admin.site.register(TopReating)
admin.site.register(Rating)
admin.site.register(Reviews)
