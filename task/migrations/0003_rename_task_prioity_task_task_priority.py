# Generated by Django 5.0.1 on 2024-01-09 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_task_prioity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_prioity',
            new_name='task_priority',
        ),
    ]
