from django import forms
from dynamic_forms import DynamicField, DynamicFormMixin
from .models import Band, Course, Module, Complaint


class classGenreChoiceForm(forms.Form):

    GENRE_CHOICES = [
        (genre, genre)
        for genre in Band.objects.values_list("genre", flat=True).distinct()
    ]

    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    genres = forms.MultipleChoiceField(
        choices=GENRE_CHOICES, widget=forms.CheckboxSelectMultiple()
    )


# From Video 4 Sample
class UniversityForm(DynamicFormMixin, forms.Form):
    def module_choices(form):
        course = form["course"].value()
        return Module.objects.filter(course=course)

    def initial_module(form):
        course = form["course"].value()
        return Module.objects.filter(course=course).first()

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), initial=Course.objects.first()
    )
    modules = DynamicField(
        forms.ModelChoiceField, queryset=module_choices, initial=initial_module
    )


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ("text", "email")
        lables = {
            "text": "Complaint",
        }
