from django import forms

from .models import Reviews, Rating, TopReating


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    top = forms.ModelChoiceField(
        queryset=TopReating.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("top",)

