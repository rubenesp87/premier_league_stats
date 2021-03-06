# Generated by Django 3.0.3 on 2020-02-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_team_total_goal_half_time_as_away',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='away_team_total_goal_second_half_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='away_team_total_goal_second_half_time_as_away',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_total_goal_second_half_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_total_goal_second_half_time_as_home',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
