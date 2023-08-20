# Generated by Django 4.2.2 on 2023-07-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmers", "0002_alter_item_picture"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loan",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.TextField()),
                ("sop", models.TextField()),
                ("ask_amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]