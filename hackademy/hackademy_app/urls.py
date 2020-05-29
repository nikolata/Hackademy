from django.urls import path, include

from hackademy_app.views import index, courses, lectures

app_name = 'hackademy_app'

courses_patterns = [
    path('', courses.list, name='list'),
    path('<int:course_id>/', courses.detail, name='detail'),
    path('new/', courses.CourseCreateView.as_view(), name='create'),
    # path('^update_book/(?P<pk>[\w-]+)', courses.UpdateCourseView.as_view(), name='update')
]

lecture_patterns = [
    path('', courses.list, name='list'),
    path('all', lectures.list, name='list'),
    path('<uuid:lecture_id>/', lectures.detail, name='detail'),
    path('new', lectures.LectureCreateView.as_view(), name='create'),
]

urlpatterns = [
    path('', index, name='index'),
    path('courses/', include((courses_patterns, 'courses'))),
    path('lectures/', include((lecture_patterns, 'lectures')))
]
