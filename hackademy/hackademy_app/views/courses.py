from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from hackademy_app.models import Courses, Lectures


def list(request):
    return render(request, 'courses/list.html', {'courses': Courses.objects.all()})


def detail(request, course_id):
    coursee = get_object_or_404(Courses, id=course_id)
    lectures = Lectures.objects.all().filter(course=course_id)
    return render(request, 'courses/detail.html', {'course': coursee, 'lectures': lectures})


class CourseCreateView(CreateView):
    model = Courses
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'courses/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('hackademy_app:courses:detail', kwargs={'course_id': self.object.id})


# class UpdateCourseView(UpdateView):
#     model = Courses
#     fields = ['name', 'description', 'start_date', 'end_date']
#     template_name = 'courses/update.html'

#     def get_success_url(self, **kwargs):
#         return reverse_lazy('hackademy_app:courses:update', kwargs={'course_id': self.object.id})
