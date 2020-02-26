# Generated by Django 2.2.10 on 2020-02-26 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0005_auto_20200226_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_corners',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_corners_as_away',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_fouls_commited',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_fouls_commited_as_away',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_goal_full_time',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_goal_full_time_as_away',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_goal_half_time',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_goal_half_time_as_away',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_goal_second_half_time',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_goal_second_half_time_as_away',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_shots',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_shots_as_away',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_shots_on_target',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team_total_shots_on_target_as_away',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_corners',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_corners_as_home',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_fouls_commited',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_fouls_commited_as_home',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_goal_full_time',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_goal_full_time_as_home',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_goal_half_time',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_goal_half_time_as_home',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_goal_second_half_time',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_goal_second_half_time_as_home',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_shots',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_shots_as_home',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_shots_on_target',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_total_shots_on_target_as_home',
        ),
        migrations.CreateModel(
            name='Totals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_total_goal_full_time', models.IntegerField()),
                ('away_team_total_goal_full_time', models.IntegerField()),
                ('home_team_total_goal_full_time_as_home', models.IntegerField()),
                ('away_team_total_goal_full_time_as_away', models.IntegerField()),
                ('home_team_total_goal_half_time', models.IntegerField()),
                ('away_team_total_goal_half_time', models.IntegerField()),
                ('home_team_total_goal_half_time_as_home', models.IntegerField()),
                ('away_team_total_goal_half_time_as_away', models.IntegerField()),
                ('home_team_total_goal_second_half_time', models.IntegerField()),
                ('away_team_total_goal_second_half_time', models.IntegerField()),
                ('home_team_total_goal_second_half_time_as_home', models.IntegerField()),
                ('away_team_total_goal_second_half_time_as_away', models.IntegerField()),
                ('home_team_total_shots', models.IntegerField()),
                ('away_team_total_shots', models.IntegerField()),
                ('home_team_total_shots_as_home', models.IntegerField()),
                ('away_team_total_shots_as_away', models.IntegerField()),
                ('home_team_total_shots_on_target', models.IntegerField()),
                ('away_team_total_shots_on_target', models.IntegerField()),
                ('home_team_total_shots_on_target_as_home', models.IntegerField()),
                ('away_team_total_shots_on_target_as_away', models.IntegerField()),
                ('home_team_total_fouls_commited', models.IntegerField()),
                ('away_team_total_fouls_commited', models.IntegerField()),
                ('home_team_total_fouls_commited_as_home', models.IntegerField()),
                ('away_team_total_fouls_commited_as_away', models.IntegerField()),
                ('home_team_total_corners', models.IntegerField()),
                ('away_team_total_corners', models.IntegerField()),
                ('home_team_total_corners_as_home', models.IntegerField()),
                ('away_team_total_corners_as_away', models.IntegerField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='football.Match')),
            ],
        ),
    ]
