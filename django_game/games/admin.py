from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import Category, Developer, Genre, Game, GameShorts, Rating, Reviews, TopReating


from ckeditor_uploader.widgets import CKEditorUploadingWidget

class GameAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Game
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("name", "url")
    list_display_links = ("name",)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Игры"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category",)
    search_fields = ("title", "category__name")
    list_editable = ("draft",)
    form = GameAdminForm


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("game", "name", "email", "text")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    """Разработчик"""
    list_display = ("name", "description", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} widht="100" height="100"')
    get_image.short_description = "Изображение"



@admin.register(GameShorts)
class GameShortsAdmin(admin.ModelAdmin):
    """Кадры к игре"""
    list_display = ("title", "games", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} widht="100" height="100"')
    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("ip", "top", "game")


admin.site.register(TopReating)


admin.site.site_title = "Django Games"
admin.site.site_header = "Django Games"


# admin.site.register(Category)
# admin.site.register(Developer)
# admin.site.register(Genre)
# admin.site.register(Game)
# admin.site.register(GameShorts)
# admin.site.register(Rating)
# admin.site.register(Reviews)
