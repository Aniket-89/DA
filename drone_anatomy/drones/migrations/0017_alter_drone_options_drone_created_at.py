# Generated by Django 4.2.11 on 2024-05-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drones", "0016_alter_droneimage_caption"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="drone",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Drone",
                "verbose_name_plural": "Drones",
            },
        ),
        migrations.AddField(
            model_name="drone",
            name="created_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]