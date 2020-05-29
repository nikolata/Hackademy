from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from hackademy_app.models import Courses, Lectures


def list(request):
    return render(request, 'lectures/list.html', {'courses': Courses.objects.all(), 'lectures': Lectures.objects.all()})


def detail(request, lecture_id):
    lecture = get_object_or_404(Lectures, lecture_id=lecture_id)
    courses = Courses.objects.all()
    return render(request, 'lectures/detail.html', {'lecture': lecture, 'coursess': courses})


class LectureCreateView(CreateView):
    model = Lectures
    fields = ['name', 'week', 'course', 'url']
    template_name = 'lectures/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('hackademy_app:lectures:detail', kwargs={'lecture_id': self.object.lecture_id})
