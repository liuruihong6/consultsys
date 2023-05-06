# Generated by Django 4.2 on 2023-04-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='custom3',
            fields=[


                ('投保人', models.CharField(blank=True, max_length=200, null=True)),
                ('保单号', models.CharField(blank=True, max_length=200, null=True)),
                ('性别', models.CharField(blank=True, max_length=200, null=True)),
                ('年龄', models.CharField(blank=True, max_length=200, null=True)),
                ('身份证', models.CharField(blank=True, max_length=200, null=True)),
                ('电话号', models.CharField(blank=True, max_length=200, null=True)),
                ('邮箱', models.EmailField(blank=True, max_length=200, null=True)),
                ('家庭住址', models.CharField(blank=True, max_length=200, null=True)),
                ('投保时间', models.DateField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': '保单信息/保单信息',
            },
        ),
    ]
