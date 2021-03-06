# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('descriptions', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=50)),
                ('required_skills', models.CharField(max_length=50)),
                ('locations', models.CharField(max_length=50)),
                ('min_education', models.CharField(max_length=50)),
                ('min_experience', models.CharField(max_length=50)),
                ('age_requirements', models.CharField(max_length=50)),
                ('gender', models.CharField(default=b'M', max_length=2)),
                ('closing_date', models.DateField()),
                ('status', models.CharField(max_length=2)),
                ('salary', models.PositiveIntegerField()),
                ('additional_benefits', models.CharField(max_length=50)),
                ('document', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='jobs',
            name='document',
            field=models.FileField(default=0, upload_to=b''),
            preserve_default=False,
        ),
    ]
