from django_mongoengine import Document
from django_mongoengine import fields


class Student(Document):
    sid = fields.StringField(max_length=255, primary_key=True, editable=True)
    name = fields.StringField(max_length=255)
    sex = fields.StringField(max_length=255)
    age = fields.StringField(max_length=255)
    birthday = fields.DateTimeField()
    dname = fields.StringField(max_length=255)
    class_name = fields.StringField(db_field='class', max_length=255)


class Teacher(Document):
    tid = fields.StringField(max_length=255, primary_key=True, editable=True)
    name = fields.StringField(max_length=255)
    sex = fields.StringField(max_length=255)
    age = fields.StringField(max_length=255)
    dname = fields.StringField(max_length=255)


class Course(Document):
    cid = fields.StringField(max_length=255, primary_key=True, editable=True)
    name = fields.StringField(max_length=255)
    fcid = fields.StringField(max_length=255, default=None, null=True, blank=True)
    credit = fields.StringField(max_length=255)


class StudentCourse(Document):
    sid = fields.StringField(max_length=255)
    cid = fields.StringField(max_length=255)
    score = fields.StringField(max_length=255)
    tid = fields.StringField(max_length=255)


class TeacherCourse(Document):
    cid = fields.StringField(max_length=255)
    tid = fields.StringField(max_length=255)
