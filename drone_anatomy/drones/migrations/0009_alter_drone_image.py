# Generated by Django 4.2.11 on 2024-05-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drones", "0008_remove_drone_img_drone_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drone",
            name="image",
            field=models.ImageField(
                default="static/drones/img/default.png", upload_to="static/drones/img"
            ),
        ),
    ]