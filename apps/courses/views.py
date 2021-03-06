# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from courses.models import Course
from operation.models import UserFavorite
from utils.is_has_fav import has_fav


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        sort = request.GET.get("sort", "")
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by("-learn_students_nums")
            elif sort == 'hot':
                all_courses = all_courses.order_by("-click_nums")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 6, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': courses,
            'hot_courses': hot_courses,
            'sort': sort,
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        is_course_has_fav = False
        is_course_org_has_fav = False

        if request.user.is_authenticated():
            if UserFavorite.objects.get(request.user, int(course_id), 1):
                is_course_has_fav = True
            if UserFavorite.objects.get(request.user, course.course_org.id, 2):
                is_course_org_has_fav = True

        # 增加课程点击数
        course.click_nums += 1
        course.save()

        # 获取相关课程
        tag = course.tag
        if tag:
            relate_course = Course.objects.filter(tag=tag)[:2]
        else:
            relate_course = []

        return render(request, 'course-detail.html', {
            'course': course,
            'relate_course': relate_course,
            'is_course_has_fav': is_course_has_fav,
            'is_course_org_has_fav': is_course_org_has_fav,
        })