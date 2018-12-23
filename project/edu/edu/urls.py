from django.conf.urls import url
from django.conf.urls import include
from django_mongoengine import mongo_admin
from rest_framework import routers
router = routers.SimpleRouter()

from edu import views as edu_views
from django.conf.urls.static import static
from django.conf import settings

# app views and viewsets
router.register(r'student', edu_views.StudentViewSet, r"student")
router.register(r'teacher', edu_views.TeacherViewSet, r"teacher")
router.register(r'course', edu_views.CourseViewSet, r"course")
router.register(r'teacher_course', edu_views.TeacherCourseViewSet, r"teacher_course")
router.register(r'student_course', edu_views.StudentCourseViewSet, r"student_course")
# router.register(r't_list', CourseSelectionViewSet, r"t_list")



urlpatterns = [
    url(r'^', mongo_admin.site.urls),
    url(r'^api/', include((router.urls, 'api'), namespace='api')),
    url(r'^api-auth/', include(('rest_framework.urls', 'rest_framework.urls'), namespace='rest_framework')),

    url(r'^show/all_choosen_courses/$', edu_views.all_choosen_courses),
    url(r'^show/course_analyse/$', edu_views.course_analyse),
    url(r'^show/score_pie/(?P<sid>[0-9]*)/$', edu_views.score_pie),

    url(r'^get_all_choosen_course_names/$', edu_views.get_all_choosen_course_names, name='get_all_choosen_course_names'),
    url(r'^get_all_courses_analyse_data/$', edu_views.get_all_courses_analyse_data, name='get_all_courses_analyse_data'),
    url(r'^get_student_scroe_pie_data/(?P<sid>[0-9]*)/$', edu_views.get_student_scroe_pie_data, name="get_student_scroe_pie_data"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

