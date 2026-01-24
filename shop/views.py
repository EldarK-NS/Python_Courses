from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import models

# Create your views here.


def index(request):
    courses = models.Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def single_course(request, course_id):
    try:
        course = models.Course.objects.get(pk=course_id)
        return render(request, 'single_course.html', {'course': course})
    except models.Course.DoesNotExist:
        raise Http404("Course not found")
