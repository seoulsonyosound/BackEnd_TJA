from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.list_students, name='list_students'),
    path('students/register/', views.register_student, name='register_student'),
]