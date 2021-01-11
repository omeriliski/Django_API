from django.shortcuts import render
from django.http import JsonResponse
from fscohort.models import Student
from django.core.serializers import serialize

def student_list(request):
    if request.method=="GET":
        students = Student.objects.all()
        students_data = serialize("python",students)
        students_count = Student.objects.count()
        data={
            "students":students_data,
            "count":students_count
        }
        return JsonResponse(data)





