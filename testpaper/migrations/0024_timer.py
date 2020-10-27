# Generated by Django 3.1 on 2020-09-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpaper', '0023_auto_20200913_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('test_name', models.CharField(max_length=50)),
                ('time_left', models.PositiveSmallIntegerField()),
            ],
        ),
    ]