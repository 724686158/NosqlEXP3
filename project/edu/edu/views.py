from rest_framework import views, mixins, permissions, exceptions
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from rest_framework import parsers, renderers

from edu.serializers import *
from edu.models import *

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class StudentViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()



class TeacherViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all()


class CourseViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()


class StudentCourseViewSet(viewsets.ModelViewSet):
    serializer_class = StudentCourseSerializer

    def get_queryset(self):
        return StudentCourse.objects.all()


class TeacherCourseViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherCourseSerializer

    def get_queryset(self):
        return TeacherCourse.objects.all()

#
# class CourseSelectionViewSet(viewsets.GenericAPIView):
#
#
#     def get_queryset(self):
#         return Teacher.objects.all()
