from django import forms
from .models import Band


class classGenreChoiceForm(forms.Form):

    GENRE_CHOICES = [
        (genre, genre)
        for genre in Band.objects.values_list("genre", flat=True).distinct()
    ]

    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    genres = forms.MultipleChoiceField(
        choices=GENRE_CHOICES, widget=forms.CheckboxSelectMultiple()
    )
