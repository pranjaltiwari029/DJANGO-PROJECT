# Generated by Django 4.2.5 on 2023-12-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor", "0004_alter_vendor_vendor_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="vendor_slug",
            field=models.SlugField(max_length=100),
        ),
    ]
