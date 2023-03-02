from django.db import models

# Create your models here.

from django.db import models


class TestData(models.Model):
    """测试数据表"""

    is_choices = (
        (1, "是"),
        (2, "否"),
    )

    system_choices = (
        (1, "案款系统"),
        (2, "涉众系统"),
        (3, "法银系统"),
        (4, "易案款"),
    )

    # 发布名称
    c_version = models.CharField(verbose_name="版本号", max_length=16)

    # 发布系统
    n_systemtype = models.SmallIntegerField(verbose_name="发布系统", choices=system_choices, default=1)

    # 发布日期
    dt_publish_date = models.DateField(verbose_name="发布日期")

    # 缺陷密度
    n_qxmd = models.DecimalField(verbose_name="缺陷密度", max_digits=10, decimal_places=2)

    # 缺陷数量
    n_qxsl = models.IntegerField(verbose_name="缺陷数量")

    # 容易缺陷
    n_ryqx = models.IntegerField(verbose_name="容易缺陷")

    # 严重缺陷
    n_yzqx = models.IntegerField(verbose_name="严重缺陷")

    # 一次性关闭率
    n_ycxgbl = models.DecimalField(verbose_name="一次性关闭率", max_digits=10, decimal_places=2)

    # 是否需求评审
    is_xqps = models.SmallIntegerField(verbose_name="是否需求评审", choices=is_choices, default=1)

    # 是否需求传递
    is_xqcd = models.SmallIntegerField(verbose_name="是否需求传递", choices=is_choices, default=1)

    # 是否设计评审
    is_sjps = models.SmallIntegerField(verbose_name="是否设计评审", choices=is_choices, default=1)

    # 是否测试用例评审
    is_csylps = models.SmallIntegerField(verbose_name="是否测试用例评审", choices=is_choices, default=1)

    # 是否性能评估
    is_xnpg = models.SmallIntegerField(verbose_name="是否性能评估", choices=is_choices, default=1)

    # 是否需求验证
    is_xqyz = models.SmallIntegerField(verbose_name="是否需求验证", choices=is_choices, default=1)

    # 是否提测演示
    is_tcys = models.SmallIntegerField(verbose_name="是否提测演示", choices=is_choices, default=1)

    # 是否测试环境测试
    is_cehjcs = models.SmallIntegerField(verbose_name="是否测试环境测试", choices=is_choices, default=1)

    # 是否稳定环境测试
    is_wdhjcs = models.SmallIntegerField(verbose_name="是否稳定环境测试", choices=is_choices, default=1)


class OrderData(models.Model):
    area_choices = (
        (1, "吉林"),
        (2, "湖南"),
        (3, "江西"),
        (4, "广西"),
        (5, "西藏"),
    )

    c_id = models.BigAutoField(primary_key=True)
    d_month = models.DateField(verbose_name="工单月份")
    c_area = models.SmallIntegerField(verbose_name="统计地区", choices=area_choices, default=1)
    c_ordertotal = models.IntegerField(verbose_name="工单数量")
