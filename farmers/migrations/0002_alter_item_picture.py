# Generated by Django 4.2.2 on 2023-07-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
