# Generated by Django 4.1 on 2023-02-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_data', '0004_rename_is_tcys_testdata_yis_tcys_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderData',
            fields=[
                ('c_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('d_month', models.DateField(verbose_name='工单月份')),
                ('c_area', models.SmallIntegerField(choices=[(1, '吉林'), (2, '湖南'), (3, '江西'), (4, '广西'), (5, '西藏')], default=1, verbose_name='统计地区')),
                ('c_ordertotal', models.IntegerField(verbose_name='工单数量')),
            ],
        ),
        migrations.AlterField(
            model_name='testdata',
            name='is_cehjcs',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否测试环境测试'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='is_csylps',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否测试用例评审'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='is_sjps',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否设计评审'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='is_wdhjcs',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否稳定环境测试'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='is_xnpg',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否性能评估'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='is_xqcd',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否需求传递'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='is_xqps',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否需求评审'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='is_xqyz',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否需求验证'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='yis_tcys',
            field=models.SmallIntegerField(choices=[(1, '是'), (2, '否')], default=1, verbose_name='是否提测演示'),
        ),
    ]
