from django.core.management.base import BaseCommand
from django.db.models import Q
from football.models import Match

POINTS_HOME = {
    "H": 3,
    "D": 1,
    "A": 0,
}

POINTS_AWAY = {
    "H": 0,
    "D": 1,
    "A": 3,
}

class Command(BaseCommand):
    help = 'Populate totals with last stats'

    def __init__(self, *args, **kwargs):
        # Result last n matches
        self.last_3_matches = {}
        self.wins_last_5_matches = {}
        self.wins_last_7_matches = {}
        self.draws_last_3_matches = {}
        self.draws_last_5_matches = {}
        self.draws_last_7_matches = {}
        self.losses_last_3_matches = {}
        self.losses_last_5_matches = {}
        self.losses_last_7_matches = {}
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        self.check_last_matches()

    def check_last_matches(self):
        matches = Match.objects.order_by('date').reverse()
        for row in matches:
            home_wins_last_3_matches = 0
            away_wins_last_3_matches = 0
            home_team_matches = Match.objects.order_by('date').filter(Q(home_team__exact=row.home_team) | Q(away_team__exact=row.home_team)).reverse()
            away_team_matches = Match.objects.order_by('date').filter(Q(home_team__exact=row.away_team) | Q(away_team__exact=row.away_team)).reverse()
            for i in range(1, 4):
                print(home_team_matches[i].home_team + " - " + home_team_matches[i].away_team)
                print(str(home_team_matches[i].full_time_home_goals) + " - " + str(home_team_matches[i].full_time_away_goals) + " - " + home_team_matches[i].full_time_result)
                if home_team_matches[i].home_team == row.home_team:
                    self.last_3_matches[row.home_team] = self.last_3_matches.get(row.home_team, 0) + POINTS_HOME[home_team_matches[i].full_time_result]

                if home_team_matches[i].away_team == row.home_team:
                    self.last_3_matches[row.home_team] = self.last_3_matches.get(row.away_team, 0) + POINTS_AWAY[home_team_matches[i].full_time_result]

            for i in range(1, 4):
                print(home_team_matches[i].home_team + " - " + home_team_matches[i].away_team)
                print(str(home_team_matches[i].full_time_home_goals) + " - " + str(home_team_matches[i].full_time_away_goals) + " - " + home_team_matches[i].full_time_result)
                if away_team_matches[i].home_team == row.away_team:
                    self.last_3_matches[row.away_team] = self.last_3_matches.get(row.away_team, 0) + POINTS_HOME[away_team_matches[i].full_time_result]

                if away_team_matches[i].away_team == row.home_team:
                    self.last_3_matches[row.away_team] = self.last_3_matches.get(row.away_team, 0) + POINTS_AWAY[away_team_matches[i].full_time_result]

                # print(home_team_matches[i].home_team + " - " + home_team_matches[i].away_team)
                # print(away_team_matches[i].home_team + " - " + away_team_matches[i].away_team)
            print(self.last_3_matches)
            break
