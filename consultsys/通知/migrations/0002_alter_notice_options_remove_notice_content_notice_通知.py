# Generated by Django 4.2 on 2023-04-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('通知', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name_plural': '审核员通知'},
        ),
        migrations.RemoveField(
            model_name='notice',
            name='content',
        ),
        migrations.AddField(
            model_name='notice',
            name='通知',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
