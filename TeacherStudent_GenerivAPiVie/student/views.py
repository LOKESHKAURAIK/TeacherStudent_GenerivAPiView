from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .StudentSerializer import StuSreializer


class StudentApi(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StuSreializer


class StudentRetUpdDestApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StuSreializer
