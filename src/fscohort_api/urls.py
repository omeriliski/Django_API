from django.urls import path
from .views import student_list,student_create,student_list_create,student_get_update_delete

urlpatterns=[
    path("student_list/",student_list),
    path("student_create/",student_create),
    path("student_list_create/",student_list_create),
    path("<int:id>",student_get_update_delete)
]