# Generated by Django 4.2.11 on 2024-05-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_alter_blog_banner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="banner",
            field=models.ImageField(blank=True, null=True, upload_to="blogs/banner"),
        ),
    ]
