# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='main_colour',
            field=models.CharField(choices=[('#000000', 'black'), ('#808080', 'gray'), ('#C0C0C0', 'silver'), ('#FFFFFF', 'white'), ('#800000', 'maroon'), ('#FF0000', 'red'), ('#808000', 'olive'), ('#FFFF00', 'yellow'), ('#008000', 'green'), ('#00FF00', 'lime'), ('#008080', 'teal'), ('#00FFFF', 'aqua'), ('#000080', 'navy'), ('#0000FF', 'blue'), ('#800080', 'purple'), ('#FF00FF', 'funchsia')], default='#FFFFFF', max_length=7),
        ),
    ]