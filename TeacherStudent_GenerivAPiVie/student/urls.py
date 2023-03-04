from django.urls import path
from .views import StudentApi, StudentRetUpdDestApi

urlpatterns = [
    path("student/",StudentApi.as_view()),
    path("student/<int:pk>",StudentRetUpdDestApi.as_view()),

]
