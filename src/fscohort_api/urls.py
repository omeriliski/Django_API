from django.urls import path
from .views import student_list,student_create,student_list_create

urlpatterns=[
    path("student_list/",student_list),
    path("student_create/",student_create),
    path("student_list_create/",student_list_create)
]