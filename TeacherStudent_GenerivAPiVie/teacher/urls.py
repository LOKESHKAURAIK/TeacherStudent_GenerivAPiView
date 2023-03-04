from django.urls import path
from .views import TeacherApi, TeacherRetUpdDestApi

urlpatterns = [
    path("teacher",TeacherApi.as_view()),
    path("teacher/<int:pk>",TeacherRetUpdDestApi.as_view()),

]
