# Generated by Django 3.1 on 2020-08-30 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testpaper', '0004_auto_20200830_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswers',
            name='correct_answer_blank',
        ),
        migrations.RemoveField(
            model_name='useranswers',
            name='user_answer_blank',
        ),
    ]
