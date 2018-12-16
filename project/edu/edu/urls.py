from django.conf.urls import url
from django.conf.urls import include
from django_mongoengine import mongo_admin
from rest_framework import routers
router = routers.SimpleRouter()

from edu.views import *

# app views and viewsets
router.register(r'student', StudentViewSet, r"student")
router.register(r'teacher', TeacherViewSet, r"teacher")
router.register(r'course', CourseViewSet, r"course")
router.register(r'teacher_course', TeacherCourseViewSet, r"teacher_course")
router.register(r'student_course', StudentCourseViewSet, r"student_course")


urlpatterns = [
    url(r'^', mongo_admin.site.urls),
    url(r'^api/', include((router.urls, 'api'), namespace='api')),
    url(r'^api-auth/', include(('rest_framework.urls', 'rest_framework.urls'), namespace='rest_framework')),

]
