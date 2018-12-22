from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from edu.models import *


class StudentSerializer(DocumentSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(DocumentSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


class CourseSerializer(DocumentSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class StudentCourseSerializer(DocumentSerializer):

    class Meta:
        model = StudentCourse
        fields = '__all__'


class TeacherCourseSerializer(DocumentSerializer):

    class Meta:
        model = TeacherCourse
        fields = '__all__'

