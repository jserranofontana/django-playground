from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import ComplaintForm
from .models import Complaint

from .models import Band, Course, Module
from .forms import classGenreChoiceForm, UniversityForm

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


# From Video 4 Sample
def courses(request):
    form = UniversityForm()
    context = {"form": form}
    return render(request, "alpine/v3.html", context)


def modules(request):
    form = UniversityForm(request.GET)
    print(form["modules"])  # form['modules'] gives us HTML for <select>
    return HttpResponse(form["modules"])


def university(request):
    return render(request, "alpine/v3-1.html", {})


def course_list(request):
    courses = Course.objects.prefetch_related("modules").all()
    context = {"courses": courses}
    return render(request, "alpine/partials/_course-list.html", context)


def tabs(request):
    return render(request, "alpine/v4.html", {})


def complaint(request):
    form = ComplaintForm()
    context = {"form": form}
    return render(request, "alpine/v5.html", context)
