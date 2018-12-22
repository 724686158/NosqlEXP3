from django_mongoengine import mongo_admin as admin
from django.shortcuts import get_object_or_404
from edu.models import Student, Teacher, Course, StudentCourse, TeacherCourse

admin.site.site_header = '教务信息管理系统'
admin.site.site_title = '教务信息管理系统'

@admin.register(Student)
class StudentAdmin(admin.DocumentAdmin):
    search_fields = ['sid']
    list_display = ('sid', 'name', 'sex', 'age', 'birthday', 'dname', 'class_name')


@admin.register(Teacher)
class TeacherAdmin(admin.DocumentAdmin):
    search_fields = ['sex', 'dname']
    list_display = ('tid', 'name', 'sex', 'age', 'dname')


@admin.register(Course)
class CourseAdmin(admin.DocumentAdmin):
    search_fields = ['fcid']
    list_display = ('cid', 'name', 'fcid', 'credit')


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.DocumentAdmin):
    search_fields = ['sid']
    list_display = ('sid', 'student_name', 'course_name', 'teacher_name', 'score')

    def course_name(self, obj):
        return get_object_or_404(Course, cid=obj.cid).name

    def teacher_name(self, obj):
        return get_object_or_404(Teacher, tid=obj.tid).name

    def student_name(self, obj):
        return get_object_or_404(Student, sid=obj.sid).name


@admin.register(TeacherCourse)
class TeacherCourseAdmin(admin.DocumentAdmin):
    search_fields = ['cid']
    list_display = ('cid', 'tid')
