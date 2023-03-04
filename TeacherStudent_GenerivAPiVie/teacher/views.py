from django.shortcuts import render
from rest_framework import generics
from .models import Teacher
from .TeacherSerializer import TeachSreializer


class TeacherApi(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeachSreializer


class TeacherRetUpdDestApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeachSreializer
