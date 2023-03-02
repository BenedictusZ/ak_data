#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 22:19
# @Author  : zhuzhengxing
# @File    : ak.py
# @Description :
import random

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

from test_data.utils.pagination import Pagination

from test_data.utils.form import TestDataModelForm, TestDataAddModelForm
from test_data.data.ak_datedeal import *


# 案款_首页面
# TODO 获取每年1-1至当前时间，返回数据给页面渲染
def ankuan_list(request):
    start = request.POST.get("start_date")
    end = request.POST.get("end_date")

    if not start:
        start = str("2023-01-01")
    if not end:
        end = str("2023-03-01")

    print("开始日期" + start)
    print("结束日期" + end)

    contex = ankuan_datedat(start, end)

    print(contex)

    return render(request, "ak.html", contex)


def ankuan_add(request):
    # 获取用户提交数据
    # response_dict = {"status": True, "msg": None}
    #
    # form_input = TestDataModelForm().errors
    # form = TestDataAddModelForm(data=request.POST).errors
    #
    # print(form_input)
    # print(form)
    #
    # try:
    #     if form.is_valid():
    #         form.save()
    # except Exception as e:
    #     response_dict['status'] = False
    #     response_dict['msg'] = str(e)
    #
    # return JsonResponse(form)
    if request.method == "GET":
        form = TestDataModelForm()
        return render(request, "ak_add.html", {"form": form})

    form = TestDataAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/ak/')
    return render(request, "ak_add.html", {"form": form})


# def ankuan_show(request):
#     queryset = TestData.objects.filter(n_systemtype=1, dt_publish_date__year=get_today_year()).all()
#     # 2.实例化分页对象
#     page_object = Pagination(request, queryset)
#
#     context = {
#         "queryset": page_object.page_queryset,  # 分完页的数据
#         "page_string": page_object.html()  # 生成页码
#     }
#
#     return render(request, "ak_show.html", context)


# TODO 动态获取需要更新参数值返回给前台
def ankuan_changedate(request):
    start = request.POST.get("start_date")
    end = request.POST.get("end_date")

    print("change:开始日期" + start)
    print("change:结束日期" + end)

    if not start:
        start = str("2023-01-01")
    if not end:
        end = str("2023-03-01")

    print("开始日期" + start)
    print("结束日期" + end)

    contex = ankuan_datedat(start, end)

    get_bbs = contex["ak_bbs"]
    get_qxzs = contex["ak_qxzs"]
    get_pjqxmd = contex["ak_pjqxmd"]
    get_pjycxgbl = contex["ak_pjycxgbl"]

    result = {
        'status': True,
        'age': get_bbs,
        'qxzs': get_qxzs,
        'pjqxmd': get_pjqxmd,
        'pjycxgbl': get_pjycxgbl,
    }

    return JsonResponse(result)


def ankuan_changedate_bar1(request):
    start = request.POST.get("start_date")
    end = request.POST.get("end_date")

    queryset = TestData.objects.filter(dt_publish_date__gte=start, dt_publish_date__lte=end,
                                       n_systemtype=1).all().order_by(
        'dt_publish_date').all()

    get_data_list = []

    for i in range(queryset.count()):
        get_data_list.append(str(queryset[i].c_version))

    qxmd = []

    # 获取 缺陷密度
    for k in range(queryset.count()):
        qxmd.append(queryset[k].n_qxmd)

    series_list = [
        {
            "data": qxmd,
            "type": 'line',
            "stack": 'x',
            "name": "缺陷密度",
            "label": {
                "show": "true",
                "position": 'top',
                "textStyle": {
                    "fontSize": 10
                }
            }
        },
        {
            "data": [],
            "type": 'line',
            "stack": 'x',
            "name": "一次性关闭率",
            "label": {
                "show": "true",
                "position": 'top',
                "textStyle": {
                    "fontSize": 10
                }
            }
        }
    ]

    for i in range(queryset.count()):
        series_list[0]["data"].append(queryset[i].n_qxmd)
        series_list[1]["data"].append(queryset[i].n_ycxgbl)

    result = {
        "status": True,
        "data": {
            'status': True,
            'series_list': series_list,
            'x_axis': get_data_list,
        },

    }
    print("---------------")
    print("sre:" + str(series_list))
    print("x_axis:" + str(get_data_list))

    return JsonResponse(result)


def ankuan_dataadd(request):
    form = TestDataAddModelForm
    return render(request, "data_add.html", {"form": form})


def ankuan_bar1(request):
    """ 迭代缺陷折线图"""

    start = str(get_today_year()) + str("-01") + str("-01")
    end = get_today_day()

    queryset = TestData.objects.filter(dt_publish_date__gte=start,
                                       dt_publish_date__lte=end,
                                       n_systemtype=1).all().order_by(
        'dt_publish_date').all()

    # 1、根据获取到的数据生成坐标轴
    # 1.1 生成日期字典值
    get_data_list = []

    # for i in range(queryset.count()):
    #     get_data_list.append(str(queryset[i].dt_publish_date)[0:7])
    #
    # # 1.2 日志字典值组装成日期列表
    # data_list = sorted(get_data_list, key=lambda date: data_processing.get_date_sort(date))
    # print(data_list)

    for i in range(queryset.count()):
        get_data_list.append(str(queryset[i].c_version))

    legend = ['缺陷密度', '一次性关闭率']

    qxmd = []

    # 获取 缺陷密度
    for k in range(queryset.count()):
        qxmd.append(queryset[k].n_qxmd)

    print("测试缺陷密度：" + str(queryset[0].n_qxmd))

    # print("获取到字典的长度：" + str(queryset.count()))

    series_list = [
        {
            "data": qxmd,
            "type": 'line',
            "stack": 'x',
            "name": "缺陷密度",
            "label": {
                "show": "true",
                "position": 'top',
                "textStyle": {
                    "fontSize": 10
                }
            },
        },
        {
            "data": [],
            "type": 'line',
            "stack": 'x',
            "name": "一次性关闭率",
            "label": {
                "show": "true",
                "position": 'top',
                "textStyle": {
                    "fontSize": 10
                }
            }
        }
    ]

    for i in range(queryset.count()):
        series_list[0]["data"].append(queryset[i].n_qxmd)
        series_list[1]["data"].append(queryset[i].n_ycxgbl)

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            "data_list": get_data_list,
            'x_axis': get_data_list,
        },

    }
    return JsonResponse(result)


def ankuan_bar2(request):
    pass


def ankuan_bar_yzqx(request):
    queryset = TestData.objects.filter(dt_publish_date__year=get_today_year(),
                                       n_systemtype=1).all().order_by(
        'dt_publish_date').all()

    get_data_list = []

    for i in range(queryset.count()):
        get_data_list.append(str(queryset[i].c_version))

    get_yzqxs = []

    # 获取 严重缺陷数
    for k in range(queryset.count()):
        yzqxzb = queryset[k].n_yzqx / queryset[k].n_qxsl * 100
        get_yzqxzb = '%.2f' % yzqxzb
        get_yzqxs.append(get_yzqxzb)

    get_qxs = []
    for k in range(queryset.count()):
        get_qxs.append(queryset[k].n_qxsl)

    legend = ['严重缺陷占比', '版本缺陷数']

    series_list = [
        {
            "name": '版本缺陷数',
            "type": 'bar',
            "yAxisIndex": 0,
            "data": get_qxs,
        },
        {
            "name": '严重缺陷占比',
            "type": 'line',
            "smooth": 'true',
            "yAxisIndex": 1,
            "data": get_yzqxs
        }
    ]

    x_axis = get_data_list

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }

    }
    return JsonResponse(result)
