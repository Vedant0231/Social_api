# Generated by Django 4.1.4 on 2023-01-04 09:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usermodel",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=20)),
                ("created_at", models.TimeField(default=datetime.datetime.utcnow)),
            ],
        ),
        migrations.CreateModel(
            name="Postmodel",
            fields=[
                ("text", models.CharField(max_length=300)),
                ("created_at", models.DateTimeField(default=datetime.datetime.utcnow)),
                ("post_id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post",
                        to="api.usermodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Likemodel",
            fields=[
                ("resp_id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "like",
                    models.CharField(
                        choices=[("like", "like"), ("like", "like")],
                        default="like",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(default=datetime.datetime.utcnow)),
                ("updated_at", models.DateTimeField(default=datetime.datetime.utcnow)),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="like",
                        to="api.postmodel",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="like",
                        to="api.usermodel",
                    ),
                ),
            ],
        ),
    ]
