# Generated by Django 4.2.11 on 2024-05-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('model', models.CharField(max_length=225)),
                ('img', models.ImageField(upload_to='media/drones')),
            ],
        ),
    ]
