"""ankuan_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include
from django.urls import re_path as url

from test_data.views import ak, fy, sz, test, trash, iterative_data, order_data

urlpatterns = [
    # path('admin/', admin.site.urls)

    # 案款数据首页面
    path('ak/', ak.ankuan_list),
    path('ak/ak_add/', ak.ankuan_add),
    # path('ak/show/', ak.ankuan_show),
    # path('ak/date/', ak.ankuan_date),
    # 监听日期变化：四大数据
    path('ak/change_date/', ak.ankuan_changedate),
    # 监听日期变化：bar1
    path('ak/change_date_bar1/', ak.ankuan_changedate_bar1),

    path('ak/data_add/', ak.ankuan_dataadd),

    path('ak/bar1/', ak.ankuan_bar1),
    path('ak/bar2/', ak.ankuan_bar2),

    path('ab/yzqx/', ak.ankuan_bar_yzqx),

    # 法银页面
    path('fy/', fy.fy_list),

    # 涉众页面
    path('sz/', sz.sz_list),

    # 测试数据首页面 ,                             \\\\\\s            w2q
    path('test/', test.test_list),
    path('test/bar1/', test.test_bar1),
    path('test/bar2/', test.test_bar2),
    path('test/bar3/', test.test_bar3),

    # 迭代数据页面
    path('itdata/', iterative_data.iterativedata_show),
    path('itdata/add/', iterative_data.iterativedata_add),

    # 工单数据页面
    path('ordata/', order_data.orderdata_show),
    path('ordata/add/', order_data.orderdata_add),

    # trash
    path('trash/', trash.trash_list),
    path('trash/map1/', trash.trash_map1),
    path('trash/bar2/', trash.trash_map2),
]
