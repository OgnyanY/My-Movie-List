# Generated by Django 4.1.6 on 2023-02-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gui", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="watched",
        ),
        migrations.RemoveField(
            model_name="series",
            name="current_episode",
        ),
        migrations.RemoveField(
            model_name="series",
            name="watched",
        ),
        migrations.AddField(
            model_name="movie",
            name="year",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="series",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("ongoing", "Ongoing"), ("completed", "Completed")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="series",
            name="year_completion",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="series",
            name="year_release",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
