from django.urls import path
from .views import student_list,student_create,student_list_create,student_get_update_delete,StudentListClass,StudentGetUpdateDeleteClass

urlpatterns=[
    path("list/",student_list),
    path("create/",student_create),
    path("list_create/",student_list_create),
    # path("<int:id>/",student_get_update_delete),
    path("list_class/",StudentListClass.as_view()),
    path("<int:id>/",StudentGetUpdateDeleteClass.as_view()),
]