# Generated by Django 4.1.2 on 2022-11-04 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_timetable_update_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='update_time',
        ),
    ]
