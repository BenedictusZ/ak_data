#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 13:53
# @Author  : zhuzhengxing
# @File    : ak_datedeal.py
# @Description :

from django.shortcuts import render

from test_data.models import TestData
from test_data.utils.data_processing import *
from datetime import date, timedelta

from test_data.utils.form import TestDataModelForm


def ankuan_datedat(start, end):
    queryset = TestData.objects.filter(n_systemtype=1, dt_publish_date__gte=start,
                                       dt_publish_date__lte=end).all()

    ak_publish_count = queryset.count()

    # 2、缺陷总数
    from django.db.models import Sum
    qxzs_queryset = TestData.objects.filter(n_systemtype=1, dt_publish_date__gte=start,
                                            dt_publish_date__lte=end).all().aggregate(aa=Sum('n_qxsl'))

    ak_qxzs_sum = qxzs_queryset['aa']

    if ak_qxzs_sum == None:

        ak_qxzs_sum = 0

    # 3、平均缺陷密度
    bb_count = TestData.objects.filter(n_systemtype=1, dt_publish_date__gte=start,
                                       dt_publish_date__lte=end).all().count()
    qxmd = TestData.objects.filter(n_systemtype=1, dt_publish_date__gte=start,
                                   dt_publish_date__lte=end).all().aggregate(
        bb=Sum('n_qxmd'))

    sum_qxmd = qxmd['bb']

    if (bb_count == 0) or (sum_qxmd == 0):
        result = 0
        avg_qxmd = '%.2f' % result
    else:
        result = sum_qxmd / bb_count

        avg_qxmd = '%.2f' % result

    #

    # 4、平均一次性关闭率
    ycxgbl = TestData.objects.filter(n_systemtype=1, dt_publish_date__gte=start,
                                     dt_publish_date__lte=end).all().aggregate(
        cc=Sum('n_ycxgbl'))

    sum_ycxgbl = ycxgbl['cc']

    if (bb_count == 0) or (sum_ycxgbl == 0):
        ycx_result = 0
        avg_ycxgbl = '%.2f' % ycx_result
    else:
        ycx_result = sum_ycxgbl / bb_count

        avg_ycxgbl = '%.2f' % ycx_result

    ak_bbs = ak_publish_count
    ak_qxzs = ak_qxzs_sum
    ak_pjqxmd = avg_qxmd
    ak_pjycxgbl = avg_ycxgbl

    contex = {"ak_bbs": ak_bbs,
              "ak_qxzs": ak_qxzs,
              "ak_pjqxmd": ak_pjqxmd,
              "ak_pjycxgbl": ak_pjycxgbl,
              }

    return contex
