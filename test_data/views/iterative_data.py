#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/26 16:29
# @Author  : zhuzhengxing
# @File    : iterative_data.py
# @Description :  迭代数据列表：数据展示+数据新增、删除
from django.shortcuts import render
from test_data.models import *
from test_data.utils.pagination import Pagination
from test_data.data.ak_datedeal import *
from test_data.utils.form import TestDataModelForm, TestDataAddModelForm
from django.shortcuts import render, HttpResponse, redirect


# 迭代数据：展示页面
def iterativedata_show(request):
    queryset = TestData.objects.filter(dt_publish_date__year=get_today_year()).order_by('dt_publish_date').all()
    # 2.实例化分页对象
    page_object = Pagination(request, queryset)

    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, "iterative_data.html", context)


def iterativedata_add(request):
    if request.method == "GET":
        form = TestDataModelForm()
        return render(request, "iterative_data_add.html", {"form": form})

    form = TestDataAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/itdata/')

    return render(request, "iterative_data_add.html", {"form": form})
