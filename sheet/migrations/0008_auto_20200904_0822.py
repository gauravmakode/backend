# Generated by Django 3.1 on 2020-09-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0007_auto_20200903_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet_name',
            name='advanced_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet_name',
            name='basic_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sheet_name',
            name='foundation_user',
            field=models.BooleanField(default=False),
        ),
    ]
