from rest_framework import fields, serializers
from fscohort.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =["first_name","last_name","number"]
