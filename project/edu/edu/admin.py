from django_mongoengine import mongo_admin as admin

from edu.models import Student, Teacher, Course, StudentCourse, TeacherCourse


@admin.register(Student)
class StudentAdmin(admin.DocumentAdmin):
    search_fields = ['sid']
    list_display = ('sid', 'name', 'sex', 'age', 'birthday', 'dname', 'class_name')


@admin.register(Teacher)
class TeacherAdmin(admin.DocumentAdmin):
    search_fields = ['tid']
    list_display = ('tid', 'name', 'sex', 'age', 'dname')


@admin.register(Course)
class CourseAdmin(admin.DocumentAdmin):
    search_fields = ['cid']
    list_display = ('cid', 'name', 'fcid', 'credit')


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.DocumentAdmin):
    search_fields = ['sid']
    list_display = ('sid', 'cid', 'score', 'tid')


@admin.register(TeacherCourse)
class TeacherCourseAdmin(admin.DocumentAdmin):
    search_fields = ['cid']
    list_display = ('cid', 'tid')