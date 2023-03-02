#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/28 10:33
# @Author  : zhuzhengxing
# @File    : bootstrap.py
# @Description :
from django import forms


class Bootstrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for name, field in self.fields.items():
            # 字段中有属性，保留原来的属性，没有属性，才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootstrapModelForm(Bootstrap, forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # 循环ModelForm中的所有字段，给每个字段的插件设置
    #     for name, field in self.fields.items():
    #         # 字段中有属性，保留原来的属性，没有属性，才增加
    #         if field.widget.attrs:
    #             field.widget.attrs["class"] = "form-control"
    #             field.widget.attrs["placeholder"] = field.label
    #         else:
    #             field.widget.attrs = {
    #                 "class": "form-control",
    #                 "placeholder": field.label
    #             }

    pass


class BootstarpForm(Bootstrap, forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # 循环ModelForm中的所有字段，给每个字段的插件设置
    #     for name, field in self.fields.items():
    #         # 字段中有属性，保留原来的属性，没有属性，才增加
    #         if field.widget.attrs:
    #             field.widget.attrs["class"] = "form-control"
    #             field.widget.attrs["placeholder"] = field.label
    #         else:
    #             field.widget.attrs = {
    #                 "class": "form-control",
    #                 "placeholder": field.label
    #             }
    pass
