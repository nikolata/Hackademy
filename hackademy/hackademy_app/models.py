from django.db import models
import uuid
from .validators import validate_url
# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    @property
    def duration(self):
        if self.end_date is not None:
            durat = self.end_date - self.start_date
            days = str(durat).split(',')[0]
            only_days = days.split(' ')[0]
            if int(only_days) >= 30:
                months = int(only_days) // 30
                if months == 1:
                    return '1 month'
                return str(months) + ' months'
            return days
        return None

    def __str__(self):
        return self.name


class Lectures(models.Model):
    lecture_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    week = models.CharField(max_length=30)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    url = models.URLField(max_length=300)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lectures, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Solutions(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    date = models.DateField()
    url = models.URLField(max_length=300, validators=[validate_url])

    def __str__(self):
        return 'soluton for ' + str(self.task)
