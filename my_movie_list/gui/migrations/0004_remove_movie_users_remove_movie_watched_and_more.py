# Generated by Django 4.1.6 on 2023-02-16 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("gui", "0003_movie_watched_series_watched"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="users",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="watched",
        ),
        migrations.RemoveField(
            model_name="series",
            name="users",
        ),
        migrations.RemoveField(
            model_name="series",
            name="watched",
        ),
        migrations.AddField(
            model_name="movie",
            name="added_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="series",
            name="added_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name="movie",
            name="year",
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="series",
            name="rating",
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name="series",
            name="status",
            field=models.CharField(
                choices=[("O", "On going"), ("C", "Completed")],
                default="Completed",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="series",
            name="year_completion",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="series",
            name="year_release",
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "movies_plan_to_watch",
                    models.ManyToManyField(
                        related_name="plan_to_watch_by", to="gui.movie"
                    ),
                ),
                (
                    "movies_watched",
                    models.ManyToManyField(related_name="watched_by", to="gui.movie"),
                ),
                (
                    "series_plan_to_watch",
                    models.ManyToManyField(
                        related_name="plan_to_watch_by", to="gui.series"
                    ),
                ),
                (
                    "series_watched",
                    models.ManyToManyField(related_name="watched_by", to="gui.series"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
