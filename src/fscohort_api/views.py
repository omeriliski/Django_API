from datetime import date
from django.shortcuts import render
from django.http import JsonResponse
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status

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
@csrf_exempt
def student_create(request):
    if request.method=="POST":
        post_body = json.loads(request.body)

        # name = post_body.get("first_name")
        # last_name = post_body.get("last_name")
        # number = post_body.get("number")
        
        # student_data={
        #     "first_name":name,
        #     "last_name":last_name,
        #     "number":number
        # }
        
        student_obj = Student.objects.create(**post_body)
        data={
            "message":f"Student {student_obj.first_name} created succesfully"
        }

        return JsonResponse(data,status=201)

@api_view(["GET","POST"])
def student_list_create(request):
    if request.method == "GET":
        students= Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Student created successfully"
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


