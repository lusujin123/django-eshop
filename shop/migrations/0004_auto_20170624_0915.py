# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-24 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170624_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='mycoupon',
            field=models.IntegerField(default=0, verbose_name='\u6211\u7684\u53ef\u7528\u4f18\u60e0\u5238'),
        ),
    ]
