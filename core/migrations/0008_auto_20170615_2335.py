# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170610_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='children',
            field=models.IntegerField(blank=True, null=True, verbose_name='Did you have children (during your experience here)?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='collaborative',
            field=models.NullBooleanField(verbose_name='Did you feel this is (or was) a collaborative position?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(verbose_name='Any additional comments?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='department',
            field=models.IntegerField(choices=[(0, b'CSE'), (1, b'BBA')], verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ethnicity',
            field=models.IntegerField(choices=[(0, b'Asian'), (1, b'Black')], verbose_name='Ethnicity'),
        ),
        migrations.AlterField(
            model_name='review',
            name='gender',
            field=models.IntegerField(choices=[(0, b'Male'), (1, b'Female'), (2, b'Non-Conforming'), (3, b'Other')], verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='review',
            name='hr_text',
            field=models.TextField(verbose_name='Have you had to deal with HR and how did they handle it?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='institution',
            field=models.CharField(max_length=250, verbose_name='What institution are you reviewing?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='position',
            field=models.IntegerField(choices=[(0, b'Administrator'), (1, b'Lecturer'), (2, b'Physician'), (3, b'Professor-Adjunct'), (4, b'Professor-Assistant'), (5, b'Professor-Associate'), (6, b'Professor-Full'), (7, b'Professor-Emeritus'), (8, b'Postdoc'), (9, b'Research Associate'), (10, b'Research Scientist'), (11, b'Student-Doctoral'), (12, b"Student-Master's"), (13, b'Student-Medical Doctor'), (14, b'Technician'), (15, b'Other')], verbose_name='What is (or was) your position at that institution?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='satisfaction',
            field=models.IntegerField(verbose_name='General satisfaction (1-10)'),
        ),
    ]
