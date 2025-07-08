from django.urls import path
from . import views
from .views import (
    # API Views
    CourseListAPI, CourseDetailAPI, EnrollStudentAPI,

    # Web Views
    CourseListView, CourseDetailView, CourseCreateView,
    course_update, course_delete,
    lesson_create, lesson_update, lesson_delete,
    enroll_student, new_students,
    register, user_login, user_logout,
    mark_complete,
)

urlpatterns = [
    # -------------------- API URLs --------------------
    path('api/courses/', CourseListAPI.as_view(), name='api_course_list'),
    path('api/courses/<int:pk>/', CourseDetailAPI.as_view(), name='api_course_detail'),
    path('api/enroll/', EnrollStudentAPI.as_view(), name='api_enroll_student'),

    # -------------------- Web Views --------------------
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('create/', CourseCreateView.as_view(), name='course_create'),

    path('<int:course_id>/update/', course_update, name='course_update'),
    path('<int:course_id>/delete/', course_delete, name='course_delete'),

    path('lesson/create/', lesson_create, name='lesson_create'),
    path('lesson/<int:lesson_id>/update/', lesson_update, name='lesson_update'),
    path('lesson/<int:lesson_id>/delete/', lesson_delete, name='lesson_delete'),
    path('lesson/<int:lesson_id>/mark_complete/', mark_complete, name='mark_complete'),

    path('enroll/', enroll_student, name='enroll_student'),
    path('<int:course_id>/new_students/', new_students, name='new_students'),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
