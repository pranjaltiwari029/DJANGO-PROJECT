# Generated by Django 4.2.5 on 2023-11-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_alter_user_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="address_line_1",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="address_line_2",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="address",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
