from django.contrib import admin
from courses.models import Course, Lesson, Student

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Student)

