# Generated by Django 5.0.3 on 2024-03-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_tags_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="done_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
