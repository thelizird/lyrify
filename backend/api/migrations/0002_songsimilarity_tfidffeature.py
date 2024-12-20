# Generated by Django 5.1.3 on 2024-11-18 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SongSimilarity",
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
                ("similarity_score", models.FloatField()),
            ],
            options={"db_table": "song_similarities", "managed": False,},
        ),
        migrations.CreateModel(
            name="TfidfFeature",
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
                ("feature_name", models.CharField(max_length=255)),
                ("tfidf_value", models.FloatField()),
            ],
            options={"db_table": "tfidf_features", "managed": False,},
        ),
    ]
