# Generated by Django 4.2.11 on 2024-05-14 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("drones", "0012_specification_icon_alter_feature_icon"),
    ]

    operations = [
        migrations.CreateModel(
            name="DroneImage",
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
                ("created_at", models.DateTimeField(auto_created=True)),
                ("photo", models.ImageField(upload_to="drones/")),
                ("caption", models.TextField(blank=True, null=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                (
                    "drone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="drones.drone"
                    ),
                ),
            ],
            options={
                "ordering": ["-updated_at"],
            },
        ),
    ]
