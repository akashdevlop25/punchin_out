# Generated by Django 3.2.18 on 2023-02-23 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('punchin_out_api', '0006_auto_20230223_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeditels',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='employeeditels',
            name='hours_for_day',
        ),
        migrations.RemoveField(
            model_name='employeeditels',
            name='punch_out',
        ),
        migrations.RemoveField(
            model_name='employeeditels',
            name='punch_out_time',
        ),
        migrations.RemoveField(
            model_name='modelpunch',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='modelpunch',
            name='hours_for_day',
        ),
        migrations.RemoveField(
            model_name='modelpunch',
            name='punch_in',
        ),
        migrations.RemoveField(
            model_name='modelpunch',
            name='punch_in_time',
        ),
    ]
