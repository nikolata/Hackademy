from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from hackademy_app.models import Courses, Lectures


def list(request):
    return render(request, 'lectures/list.html', {'courses': Courses.objects.all(), 'lectures': Lectures.objects.all()})
