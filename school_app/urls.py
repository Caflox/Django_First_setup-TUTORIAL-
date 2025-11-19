from django.urls import path
from . import views 

urlpatterns = [
    path("hello-world/", views.hello_world, name="hello_world"),
    path("welcome-school/", views.school, name='welcome_school'),
    path("subjects", views.list_subjects, name='list_subjects'),
    path("subjects/<int:pk>", views.subject_detail, name="subject_detail"),
]