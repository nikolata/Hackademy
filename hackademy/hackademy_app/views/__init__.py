from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


import hackademy_app.views.courses
