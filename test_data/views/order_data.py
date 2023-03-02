#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/26 17:00
# @Author  : zhuzhengxing
# @File    : order_data.py
# @Description : 工单数据列表：数据展示+数据新增、删除

from django.shortcuts import render
from test_data.models import *
from test_data.utils.pagination import Pagination
from test_data.data.ak_datedeal import *
from test_data.utils.form import OrderDataAddModelForm
from django.shortcuts import render, HttpResponse, redirect


# 迭代数据：展示页面
def orderdata_show(request):
    queryset = OrderData.objects.filter(d_month__year=get_today_year()).all()
    # 2.实例化分页对象
    page_object = Pagination(request, queryset)

    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, "order_data.html", context)


def orderdata_add(request):
    if request.method == "GET":
        form = OrderDataAddModelForm()
        return render(request, "order_data_add.html", {"form": form})

    form = OrderDataAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/orderdata/')

    return render(request, "order_data_add.html", {"form": form})
