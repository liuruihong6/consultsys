# Generated by Django 4.2 on 2023-05-04 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('保单管理', '0004_alter_custom3_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=32, verbose_name='性别')),
            ],
        ),
    ]
