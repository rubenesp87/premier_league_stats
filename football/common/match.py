from football.models import Match
from football.common.helpers import format_date


def get_or_create_match_stats(row):
    defaults = dict(
        full_time_home_goals=row[4],
        full_time_away_goals=row[5],
        full_time_result=row[6],
        half_time_home_goals=row[7],
        half_time_away_goals=row[8],
        half_time_result=row[9],
        referee=row[10],
        home_team_shots=row[11],
        away_team_shots=row[12],
        home_team_shots_on_target=row[13],
        away_team_shots_on_target=row[14],
        home_team_fouls_commited=row[15],
        away_team_fouls_commited=row[16],
        home_team_corners=row[17],
        away_team_corners=row[18],
        home_team_yellow_cards=row[19],
        away_team_yellow_cards=row[20],
        home_team_red_cards=row[21],
        away_team_red_cards=row[22],
    )

    match, created = Match.objects.get_or_create(
        date=format_date(row[1]),
        home_team=row[2],
        away_team=row[3],
        defaults=defaults,
    )

    return match, created
