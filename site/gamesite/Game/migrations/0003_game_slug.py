# Generated by Django 3.0.7 on 2020-06-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0002_game_game_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
