# Generated by Django 4.1.7 on 2023-08-01 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("imdb_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchlist",
            name="platform",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchlist",
                to="imdb_api.streamplatform",
            ),
        ),
    ]