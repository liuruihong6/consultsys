# Generated by Django 4.2 on 2023-04-17 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('咨询', '0004_user1_alter_user_options_rename_业务员解答_user_备注'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='user1',
        ),
    ]
