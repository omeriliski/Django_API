from datetime import date
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status

# Function Base
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
        print("students",students)
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

@api_view(["GET","PUT","DELETE"])
def student_get_update_delete(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method=="PUT":
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Student updated successfully"
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class Base
class StudentListClass(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentGetUpdateDeleteClass(APIView):
    
    def get_object(self,id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        student = self.get_object(id)
        # student = get_object_or_404(Student,id=id) böyle de olur,yukarıyı yazmadan
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,id):
        student = self.get_object(id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        