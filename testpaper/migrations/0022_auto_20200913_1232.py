# Generated by Django 3.1 on 2020-09-13 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testpaper', '0021_flag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flag',
            old_name='sheet_name',
            new_name='test_ame',
        ),
    ]