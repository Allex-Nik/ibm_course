# Generated by Django 3.1.3 on 2023-06-23 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_choice_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='lesson',
        ),
    ]
