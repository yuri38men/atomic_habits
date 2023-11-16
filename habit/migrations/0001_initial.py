# Generated by Django 4.2.7 on 2023-11-16 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
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
                    "place",
                    models.CharField(max_length=255, verbose_name="место выполнения"),
                ),
                (
                    "notification_time",
                    models.CharField(
                        choices=[
                            ("fifteen", "за 15 минут"),
                            ("thirty", "за 30 минут"),
                            ("hour", "за час"),
                            ("two_hours", "за 2 часа"),
                            ("day", "за 24 часа"),
                        ],
                        default="thirty",
                        max_length=20,
                        verbose_name="уведомление до начала привычки",
                    ),
                ),
                ("time", models.TimeField(verbose_name="время выполнения привычки")),
                (
                    "action",
                    models.CharField(
                        max_length=255, verbose_name="действие (привычка)"
                    ),
                ),
                (
                    "is_reward",
                    models.BooleanField(
                        default=False, verbose_name="признак приятной привычки"
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        choices=[("daily", "ежедневная"), ("weekly", "еженедельная")],
                        default="daily",
                        max_length=20,
                        verbose_name="периодичность выполнения привычки",
                    ),
                ),
                (
                    "weekday",
                    models.CharField(
                        choices=[("today", "сегодня"), ("tomorrow", "завтра")],
                        default="today",
                        max_length=20,
                        verbose_name="cтарт выполнения привычки",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name="вознаграждение за выполнение привычки",
                    ),
                ),
                (
                    "estimated_time",
                    models.IntegerField(verbose_name="время на выполнение привычки"),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="признак публичности привычки"
                    ),
                ),
                (
                    "date_of_start",
                    models.DateField(
                        auto_now_add=True, verbose_name="дата начала привычки"
                    ),
                ),
                (
                    "is_starting",
                    models.BooleanField(
                        default=False, verbose_name="признак начала рассылки"
                    ),
                ),
                (
                    "notification",
                    models.CharField(
                        choices=[
                            ("telegram", "телеграм"),
                            ("email", "электронная почта"),
                        ],
                        default="telegram",
                        max_length=20,
                        verbose_name="метод оповещения",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habit.habit",
                        verbose_name="cвязанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "привычка",
                "verbose_name_plural": "привычки",
            },
        ),
    ]