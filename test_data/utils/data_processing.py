#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 22:21
# @Author  : zhuzhengxing
# @File    : data_processing.py
# @Description : 数据处理相关插件地址

import datetime


# 获取当年
def get_today_year():
    today = datetime.datetime.today()
    year = today.year
    return year


def get_today_month():
    today = datetime.datetime.today()
    year = today.month
    return year


def get_today_day():
    today = datetime.datetime.today()
    return today


def get_date_sort(date):
    return datetime.datetime.strptime(date, "%Y-%m").timestamp()
