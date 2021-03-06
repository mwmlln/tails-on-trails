# Generated by Django 3.2.7 on 2021-10-13 12:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20211012_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('about_me', models.TextField(blank=True, max_length=300)),
                ('about_dog', models.TextField(blank=True, max_length=300)),
                ('favorite_location', models.TextField(blank=True, max_length=50)),
            ],
        ),
    ]
