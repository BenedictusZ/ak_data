#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 22:04
# @Author  : zhuzhengxing
# @File    : trash.py
# @Description :


from django.shortcuts import render
from django.forms import ModelForm
from django.shortcuts import render
from django.http import JsonResponse
import datetime
from test_data.models import OrderData
from test_data.utils import data_processing

from django.db.models import Max


def trash_list(request):
    return render(request, 'trash.html')


def trash_map1(request):
    """ 构造柱状图的数据"""

    queryset = OrderData.objects.filter(d_month__year=data_processing.get_today_year()).order_by("d_month").all()

    max_value_get = OrderData.objects.filter(d_month__year=data_processing.get_today_year()).order_by(
        "d_month").all().aggregate(
        Max('c_ordertotal'))

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


def trash_map2(request):
    """ 1- 迭代缺陷折线图 """
    # 数据可以去数据库中获取
    legend = ['系统问题', '工单占比']

    series_list = [
        {
            "name": 'xx',
            "type": 'bar',
            "yAxisIndex": 0,
            "data": [10, 20, 30, 80, 58, 68, 78]
        },
        {
            "name": 'yy',
            "type": 'line',
            "smooth": 'true',
            "yAxisIndex": 1,
            "data": [17, 18, 19, 0, 18, 0]
        }
    ]

    x_axis = ['1月', '2月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)
