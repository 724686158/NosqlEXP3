from django_mongoengine import mongo_admin as admin

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
    list_display = ('sid', 'cid', 'score', 'tid')


@admin.register(TeacherCourse)
class TeacherCourseAdmin(admin.DocumentAdmin):
    search_fields = ['cid']
    list_display = ('cid', 'tid')
