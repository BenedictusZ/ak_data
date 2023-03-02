# Generated by Django 4.1 on 2023-02-15 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_data', '0002_alter_testdata_publish_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testdata',
            old_name='publish_system',
            new_name='c_publish_system',
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='version',
            new_name='c_version',
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='publish_date',
            new_name='dt_publish_date',
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='qxmd',
            new_name='n_qxmd',
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='qxsl',
            new_name='n_qxsl',
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='ryqx',
            new_name='n_ryqx',
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='ycxgbl',
            new_name='n_ycxgbl',
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='yzqx',
            new_name='n_yzqx',
        ),
    ]