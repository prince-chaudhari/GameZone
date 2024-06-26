# Generated by Django 5.0.2 on 2024-03-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameWebsite', '0009_remove_profile_checkuser_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hangman_game_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='memory_card_game_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='rock_paper_scissors_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='snake_game_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='tic_tac_toe_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
