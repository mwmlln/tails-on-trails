# Generated by Django 3.2.7 on 2021-10-16 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_alter_profile_favorite_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
