from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentapi/", include('student.urls')),
    path("teacherapi/", include('teacher.urls')),

]
