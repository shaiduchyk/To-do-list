# Generated by Django 5.0.3 on 2024-03-11 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0006_alter_task_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["done_at", "-created_at"]},
        ),
    ]
