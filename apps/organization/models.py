# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models


# Create your models here.
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市名称")
    desc = models.TextField(verbose_name="城市描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = verbose_name = "城市"

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    CATEGORY_ITEMS = (
        ('pxjg', '培训机构'),
        ('gx', '高校'),
        ('gr', '个人'),
    )

    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(max_length=20, choices=CATEGORY_ITEMS, default='pxjg', verbose_name="机构类别")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    courses = models.IntegerField(default=0, verbose_name="课程数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="封面图片", max_length=100)
    address = models.CharField(max_length=150, verbose_name="机构地址")
    city = models.ForeignKey(CityDict, verbose_name="所在城市")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = verbose_name = "课程机构"

    def __unicode__(self):
        return self.name

    def get_teacher_nums(self):
        return self.teacher_set.all().count()


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构")
    name = models.CharField(max_length=20, verbose_name="教师名称")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(default=0, max_length=100, verbose_name="就职公司")
    work_position = models.CharField(default=0, max_length=100, verbose_name="工作职位")
    image = models.ImageField(upload_to="teacher/%Y/%m", blank=True, null=True, verbose_name="头像")
    feature = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = verbose_name = "教师"

    def __unicode__(self):
        return self.name