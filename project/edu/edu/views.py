from rest_framework import permissions
from rest_framework_mongoengine import viewsets
from rest_framework.decorators import permission_classes
from edu.serializers import *
from edu.models import *
from django.http import JsonResponse

import time

from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404


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

@permission_classes((permissions.AllowAny,))
def score_pie(request, sid):
    return render(request, 'd3js_html/score_pie.html', {
        'sid': sid,
    })

@permission_classes((permissions.AllowAny,))
def course_analyse(request):
    return render(request, 'd3js_html/course_analyse.html', {
    })

@permission_classes((permissions.AllowAny,))
def all_choosen_courses(request):
    return render(request, 'd3js_html/all_choosen_courses.html', {})


@permission_classes((permissions.AllowAny,))
def get_all_choosen_course_names(request):
    t1 = time.time()
    cs_list = get_list_or_404(StudentCourse)
    t2 = time.time()
    print("学生选课列表获取耗时{:4f}s".format(t2 - t1))
    ans = {
        "names": []
    }
    cs_id_set = set(cs.cid for cs in cs_list)
    t3= time.time()
    print("list->set转换耗时{:4f}s".format(t3 - t2))
    for id in cs_id_set:
        ans["names"].append(get_object_or_404(Course, cid=id).name)
    t4 = time.time()
    print("根据id查name耗时{:4f}s".format(t4 - t3))
    return JsonResponse(ans, safe=False)

@permission_classes((permissions.AllowAny,))
def get_student_scroe_pie_data(request, sid):
    t1 = time.time()
    cs_list = get_list_or_404(StudentCourse, sid=sid)
    sname = get_object_or_404(Student, sid=sid).name
    t2 = time.time()
    print("学生选课列表获取耗时{:4f}s".format(t2 - t1))
    csv_data = []
    a = 0
    b = 0
    c = 0
    f = 0
    for cs in cs_list:
        if cs.score:
            if cs.score >= 90:
                a = a + 1
            elif cs.score >= 80 :
                b = b + 1
            elif cs.score >= 60:
                c = c + 1
            else:
                f = f + 1
        else:
            pass
    csv_data = [{
        "origin": sname,
        "carrier": "优秀{}门".format(a),
        "count": a,
      },{
        "origin": sname,
        "carrier": "良好{}门".format(b),
        "count": b,
      },{
        "origin": sname,
        "carrier": "合格{}门".format(c),
        "count": c,
      },{
        "origin": sname,
        "carrier": "不合格{}门".format(f),
        "count": f,
      }]
    t3 = time.time()
    print("成绩统计耗时{:4f}s".format(t3 - t2))
    return JsonResponse({"data": csv_data}, safe=False)

@permission_classes((permissions.AllowAny,))
def get_all_courses_analyse_data(request):
    ans = []
    t1 = time.time()
    cs_list = get_list_or_404(StudentCourse)
    t2 = time.time()
    print("学生选课列表获取耗时{:4f}s".format(t2 - t1))
    count_dict = dict()
    sum_dict = dict()
    for cs in cs_list:
        if cs.cid in count_dict:
            count_dict[cs.cid] += 1
        else:
            count_dict[cs.cid] = 1
        if cs.cid in sum_dict:
            sum_dict[cs.cid] += float(cs.score)
        else:
            sum_dict[cs.cid] = 0.0
    cs_id_set = set(cs.cid for cs in cs_list)
    t3= time.time()
    print("选课与得分统计耗时{:4f}s".format(t3 - t2))
    for id in cs_id_set:
        cname = get_object_or_404(Course, cid=id).name
        snum = count_dict[id]
        score_avg = sum_dict[id] / count_dict[id]
        ans.append({
            "cid": id,
            "cname":cname,
            "snum":snum,
            "score_avg":score_avg,
        })
    t4 = time.time()
    print("课程名获取与平均分计算耗时{:4f}s".format(t4 - t3))
    return JsonResponse(ans, safe=False)
