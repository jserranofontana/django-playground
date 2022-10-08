from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Band
from .forms import classGenreChoiceForm

# Create your views here.


def people(request):
    people = [
        {"name": "Mark", "image": "https://via.placeholder.com/150"},
        {"name": "Jeff", "image": "https://via.placeholder.com/150"},
    ]
    # import time
    # time.sleep(1)

    return JsonResponse(people, safe=False)


def index(request):
    form = classGenreChoiceForm
    context = {"form": form}
    return render(request, "alpine/v2.html", context)


def bands(request):
    bands = Band.objects.all()
    data = []
    for band in bands:
        data.append({"name": band.name, "genre": band.genre})

    return JsonResponse(data, safe=False)
