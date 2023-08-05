from audioop import reverse
from django.urls import reverse
from django.db import models

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Developer(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="Developers/")



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("developer_detail", kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчики"

class Genre(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Game(models.Model):
    objects = None
    title = models.CharField("Название игры", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    platforms = models.CharField("Платформа", max_length=20, default="Windows")
    engine = models.CharField("Двигатель", max_length=100)
    preview = models.ImageField("Превью", upload_to="games/")
    developers = models.ManyToManyField(Developer, verbose_name="разработчик", related_name="game_developer")
    year = models.PositiveSmallIntegerField("Дата выхода")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать сумму в $")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class GameShorts(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="game_shorts/")
    games = models.ForeignKey(Game, verbose_name="Игра", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из игры"
        verbose_name_plural = "Кадры из игры"

class TopReating(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Топ рейтинга"
        verbose_name_plural = "Топы рейтинга"

class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    top = models.ForeignKey(TopReating, on_delete=models.CASCADE, verbose_name="топ")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="игра", related_name="ratings")

    def __str__(self):
        return f"{self.top} - {self.game}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    game = models.ForeignKey(Game, verbose_name="игра", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.game}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"