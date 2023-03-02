#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 22:19
# @Author  : zhuzhengxing
# @File    : test.py
# @Description :
# 测试_首页面

from django.shortcuts import render
from django.http import JsonResponse
from test_data.models import *
from test_data.utils.data_processing import *
from django.db.models import Max


def test_list(request):
    return render(request, 'test.html')


def test_bar1(request):
    """ 构造柱状图的数据 """
    legend = ['梁吉宁', '武沛齐']

    series_list = [
        {
            "name": '梁吉宁',
            "type": 'bar',
            "data": [15, 20, 36, 10, 10, 10]
        },
        {
            "name": '武沛齐',
            "type": 'bar',
            "data": [45, 10, 66, 40, 20, 50]
        }
    ]
    x_axis = ['1月', '2月', '4月', '5月', '6月', '7月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def test_bar2(request):
    """ 构造柱状图的数据 """
    # 数据可以去数据库中获取
    legend = ["梁吉宁", "武沛齐"]
    series_list = [
        {
            "name": '梁吉宁',
            "type": 'bar',
            "data": [15, 20, 36, 10, 10, 10]
        },
        {
            "name": '武沛齐',
            "type": 'bar',
            "data": [45, 10, 66, 40, 20, 50]
        }
    ]
    x_axis = ['1月', '2月', '3月', '5月', '6月', '7月', '8', '9', '10', '11', '12']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def test_bar3(request):
    queryset = OrderData.objects.filter(d_month__year=get_today_year()).order_by("d_month").all()

    max_value_get = OrderData.objects.filter(d_month__year=get_today_year()).order_by(
        "d_month").all().aggregate(Max('c_ordertotal'))

    max_value = max_value_get["c_ordertotal__max"]

    get_data_list = []

    aa = {}
    for i in range(queryset.count()):
        aa["name"] = queryset[i].get_c_area_display()
        aa["value"] = str(queryset[i].c_ordertotal)

        tmp = {}
        tmp["name"] = aa["name"]
        tmp["value"] = aa["value"]
        get_data_list.append(tmp)

    print(get_data_list)

    result = {
        "status": True,
        "data": {
            # 'legend': legend,
            # 'series_list': series_list,
            "series_list": get_data_list,
            "max_value": max_value

            # 'x_axis': get_data_list,
        },

    }
    return JsonResponse(result)
