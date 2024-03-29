# Generated by Django 4.2.5 on 2023-09-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User_Profile",
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
                ("first_name", models.CharField(default="", max_length=50)),
                ("Last_name", models.CharField(default="", max_length=50)),
                ("Email", models.EmailField(max_length=50, unique=True)),
                ("Phone_no", models.IntegerField(max_length=10)),
                ("password", models.IntegerField(max_length=20)),
            ],
        ),
    ]
