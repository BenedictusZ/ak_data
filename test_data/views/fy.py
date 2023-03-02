#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 22:19
# @Author  : zhuzhengxing
# @File    : fy.py
# @Description :
from django.shortcuts import render
from django.http import JsonResponse


def fy_list(request):
    return render(request, 'fy.html')
