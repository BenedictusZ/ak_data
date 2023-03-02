#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 21:10
# @Author  : zhuzhengxing
# @File    : form.py
# @Description :

from test_data.models import OrderData, TestData

from django.core.validators import RegexValidator
from django.core.validators import ValidationError

from test_data.utils.bootstrap import BootstrapModelForm
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django import forms


class TestDataModelForm(BootstrapModelForm):
    dt_publish_date = forms.DateField(widget=DatePicker(), label="请选择发布日期")

    class Meta:
        model = TestData
        fields = "__all__"
        exclude = None  # 排除的字段
        labels = None  # 提示信息
        help_texts = None  # 帮助提示信息
        widgets = None  # 自定义插件
        error_messages = None  # 自定义错误信息


class TestDataAddModelForm(BootstrapModelForm):
    class Meta:
        model = TestData

        fields = "__all__"
        exclude = None  # 排除的字段
        labels = None  # 提示信息
        help_texts = None  # 帮助提示信息
        widgets = None  # 自定义插件
        error_messages = None  # 自定义错误信息

    def clean_c_version(self):
        txt_version = self.cleaned_data["c_version"]
        exists = TestData.objects.filter(c_version=txt_version).exists()
        print("是否存在：" + str(exists))

        if exists:
            raise ValidationError("该版本号已存在！")

        # 验证通过,用户输入的值返回
        return txt_version


class OrderDataAddModelForm(BootstrapModelForm):
    d_month = forms.DateField(widget=DatePicker(), label="请选择日期")
    class Meta:
        model = OrderData
        fields = "__all__"
