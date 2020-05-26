from django.contrib import admin
from .models import Courses, Lectures, Tasks, Solutions

# Register your models here.


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'end_date', 'duration']


@admin.register(Lectures)
class LecturesAdmin(admin.ModelAdmin):
    list_display = ['lecture_id', 'name', 'week', 'course', 'url']


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'due_date', 'course', 'lecture']


@admin.register(Solutions)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['task', 'date', 'url']
