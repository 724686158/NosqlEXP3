from django_mongoengine import Document
from django_mongoengine import fields


class Student(Document):
    sid = fields.IntField()
    name = fields.StringField(max_length=255)
    sex = fields.StringField(max_length=255)
    age = fields.IntField()
    birthday = fields.DateTimeField()
    dname = fields.StringField(max_length=255)
    class_name = fields.StringField(db_field='class', max_length=255)


class Teacher(Document):
    tid = fields.IntField()
    name = fields.StringField(max_length=255)
    sex = fields.StringField(max_length=255)
    age = fields.IntField()
    dname = fields.StringField(max_length=255)


class Course(Document):
    cid = fields.IntField()
    name = fields.StringField(max_length=255)
    fcid = fields.IntField()
    credit = fields.FloatField()


class StudentCourse(Document):
    sid = fields.IntField()
    cid = fields.IntField()
    score = fields.IntField(blank=True, null=True)
    tid = fields.IntField()


class TeacherCourse(Document):
    cid = fields.IntField()
    tid = fields.IntField()



