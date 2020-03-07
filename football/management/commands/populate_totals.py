from django.core.management.base import BaseCommand
import csv
import os
from django.conf import settings
from football.common.validation import valid_legend
from football.common.match import get_or_create_match_stats
from football.common.referee import get_or_create_referee_stats
from football.models import Totals

CSV_FILES = [
    "football/data/2010.csv",
    "football/data/2011.csv",
    "football/data/2012.csv",
    "football/data/2013.csv",
    "football/data/2014.csv",
    "football/data/2015.csv",
    "football/data/2016.csv",
    "football/data/2017.csv",
    "football/data/2018.csv",
    "football/data/2019.csv",
    "football/data/2020.csv",
]


class Command(BaseCommand):
    help = 'Populate football data'

    def __init__(self, *args, **kwargs):
        # Total goals
        self.team_total_goal_full_time = {}
        self.home_team_total_goal_full_time = {}
        self.away_team_total_goal_full_time = {}
        self.team_total_goal_half_time = {}
        self.home_team_total_goal_half_time = {}
        self.away_team_total_goal_half_time = {}
        self.team_total_goal_conceded_full_time = {}
        self.home_team_total_goal_conceded_full_time = {}
        self.away_team_total_goal_conceded_full_time = {}
        self.team_total_goal_conceded_half_time = {}
        self.home_team_total_goal_conceded_half_time = {}
        self.away_team_total_goal_conceded_half_time = {}
        # Total shots
        self.team_total_shots = {}
        self.home_team_total_shots = {}
        self.away_team_total_shots = {}
        self.team_total_shots_on_target = {}
        self.home_team_total_shots_on_target = {}
        self.away_team_total_shots_on_target = {}
        # Total shots conceded
        self.team_total_shots_conceded = {}
        self.home_team_total_shots_conceded = {}
        self.away_team_total_shots_conceded = {}
        self.team_total_shots_conceded_on_target = {}
        self.home_team_total_shots_conceded_on_target = {}
        self.away_team_total_shots_conceded_on_target = {}
        # Total fouls commited
        self.team_total_fouls_commited = {}
        self.home_team_total_fouls_commited = {}
        self.away_team_total_fouls_commited = {}
        # Total fouls conceded
        self.team_total_fouls_conceded = {}
        self.home_team_total_fouls_conceded = {}
        self.away_team_total_fouls_conceded = {}
        # Total corners
        self.team_total_corners = {}
        self.home_team_total_corners = {}
        self.away_team_total_corners = {}
        # Total corners conceded
        self.team_total_corners_conceded = {}
        self.home_team_total_corners_conceded = {}
        self.away_team_total_corners_conceded = {}
        # Total yellow cards
        self.team_total_yellow_cards = {}
        self.home_total_yellow_cards = {}
        self.away_total_yellow_cards = {}
        # Total yellow cards conceded
        self.team_total_yellow_cards_conceded = {}
        self.home_total_yellow_cards_conceded = {}
        self.away_total_yellow_cards_conceded = {}
        # Total red cards
        self.team_total_red_cards = {}
        self.home_total_red_cards = {}
        self.away_total_red_cards = {}
        # Total red cards conceded
        self.team_total_red_cards_conceded = {}
        self.home_total_red_cards_conceded = {}
        self.away_total_red_cards_conceded = {}
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        try:
            for file in CSV_FILES:
                print("Importing: " + file)
                path = os.path.join(settings.BASE_DIR, file)
                with open(path) as f:
                    reader = csv.reader(f)

                    if not valid_legend(next(reader)):
                        raise Exception()

                    for row in reader:
                        self.get_total_goals(row)
                        self.get_total_shots(row)
                        self.get_total_fouls_commited(row)
                        self.get_total_corners(row)
                        self.get_total_cards(row)
                        match, match_created = get_or_create_match_stats(row)
                        if match_created:
                            self.get_or_create_total_stats(row, match)
                            get_or_create_referee_stats(row)
        except Exception as e:
            print(e)

    def get_total_goals(self, row):
        # Total goals team
        self.team_total_goal_full_time[row[2]] = self.team_total_goal_full_time.get(row[2], 0) + int(row[4])
        self.team_total_goal_full_time[row[3]] = self.team_total_goal_full_time.get(row[3], 0) + int(row[5])
        # Total goals home / away
        self.home_team_total_goal_full_time[row[2]] = self.home_team_total_goal_full_time.get(row[2], 0) + int(row[4])
        self.away_team_total_goal_full_time[row[3]] = self.away_team_total_goal_full_time.get(row[3], 0) + int(row[5])
        # Total goals home / away first half
        self.team_total_goal_half_time[row[2]] = self.team_total_goal_half_time.get(row[2], 0) + int(row[7])
        self.team_total_goal_half_time[row[3]] = self.team_total_goal_half_time.get(row[3], 0) + int(row[8])
        # Total goals home / away second half
        self.home_team_total_goal_half_time[row[2]] = self.home_team_total_goal_half_time.get(row[2], 0) + int(row[7])
        self.away_team_total_goal_half_time[row[3]] = self.away_team_total_goal_half_time.get(row[3], 0) + int(row[8])
        # Total goals team conceded
        self.team_total_goal_conceded_full_time[row[2]] = self.team_total_goal_conceded_full_time.get(row[2], 0) + int(row[5])
        self.team_total_goal_conceded_full_time[row[3]] = self.team_total_goal_conceded_full_time.get(row[3], 0) + int(row[4])
        # Total goals home / away conceded
        self.home_team_total_goal_conceded_full_time[row[2]] = self.home_team_total_goal_conceded_full_time.get(row[2], 0) + int(row[5])
        self.away_team_total_goal_conceded_full_time[row[3]] = self.away_team_total_goal_conceded_full_time.get(row[3], 0) + int(row[4])
        # Total goals home / away first half conceded
        self.team_total_goal_conceded_half_time[row[2]] = self.team_total_goal_conceded_half_time.get(row[2], 0) + int(row[8])
        self.team_total_goal_conceded_half_time[row[3]] = self.team_total_goal_conceded_half_time.get(row[3], 0) + int(row[7])
        # Total goals home / away second half conceded
        self.home_team_total_goal_conceded_half_time[row[2]] = self.home_team_total_goal_conceded_half_time.get(row[2], 0) + int(row[8])
        self.away_team_total_goal_conceded_half_time[row[3]] = self.away_team_total_goal_conceded_half_time.get(row[3], 0) + int(row[7])

    def get_total_shots(self, row):
        # Total shots team
        self.team_total_shots[row[2]] = self.team_total_shots.get(row[2], 0) + int(row[11])
        self.team_total_shots[row[3]] = self.team_total_shots.get(row[3], 0) + int(row[12])
        # Total shots home / away
        self.home_team_total_shots[row[2]] = self.home_team_total_shots.get(row[2], 0) + int(row[11])
        self.away_team_total_shots[row[3]] = self.away_team_total_shots.get(row[3], 0) + int(row[12])
        # Total shots on target team
        self.team_total_shots_on_target[row[2]] = self.team_total_shots_on_target.get(row[2], 0) + int(row[13])
        self.team_total_shots_on_target[row[3]] = self.team_total_shots_on_target.get(row[3], 0) + int(row[14])
        # Total shots on target home / away
        self.home_team_total_shots_on_target[row[2]] = self.home_team_total_shots_on_target.get(row[2], 0) + int(row[13])
        self.away_team_total_shots_on_target[row[3]] = self.away_team_total_shots_on_target.get(row[3], 0) + int(row[14])
        # Total shots team conceded
        self.team_total_shots_conceded[row[2]] = self.team_total_shots_conceded.get(row[2], 0) + int(row[12])
        self.team_total_shots_conceded[row[3]] = self.team_total_shots_conceded.get(row[3], 0) + int(row[11])
        # Total shots home / away conceded
        self.home_team_total_shots_conceded[row[2]] = self.home_team_total_shots_conceded.get(row[2], 0) + int(row[12])
        self.away_team_total_shots_conceded[row[3]] = self.away_team_total_shots_conceded.get(row[3], 0) + int(row[11])
        # Total shots on target team conceded
        self.team_total_shots_conceded_on_target[row[2]] = self.team_total_shots_conceded_on_target.get(row[2], 0) + int(row[14])
        self.team_total_shots_conceded_on_target[row[3]] = self.team_total_shots_conceded_on_target.get(row[3], 0) + int(row[13])
        # Total shots on target home / away conceded
        self.home_team_total_shots_conceded_on_target[row[2]] = self.home_team_total_shots_conceded_on_target.get(row[2], 0) + int(row[14])
        self.away_team_total_shots_conceded_on_target[row[3]] = self.away_team_total_shots_conceded_on_target.get(row[3], 0) + int(row[13])

    def get_total_fouls_commited(self, row):
        # Total fouls commited team
        self.team_total_fouls_commited[row[2]] = self.team_total_fouls_commited.get(row[2], 0) + int(row[15])
        self.team_total_fouls_commited[row[3]] = self.team_total_fouls_commited.get(row[3], 0) + int(row[16])
        # Total fouls commited home / away
        self.home_team_total_fouls_commited[row[2]] = self.home_team_total_fouls_commited.get(row[2], 0) + int(row[15])
        self.away_team_total_fouls_commited[row[3]] = self.away_team_total_fouls_commited.get(row[3], 0) + int(row[16])
        # Total fouls conceded team
        self.team_total_fouls_conceded[row[2]] = self.team_total_fouls_conceded.get(row[2], 0) + int(row[16])
        self.team_total_fouls_conceded[row[3]] = self.team_total_fouls_conceded.get(row[3], 0) + int(row[15])
        # Total fouls conceded home / away
        self.home_team_total_fouls_conceded[row[2]] = self.home_team_total_fouls_conceded.get(row[2], 0) + int(row[16])
        self.away_team_total_fouls_conceded[row[3]] = self.away_team_total_fouls_conceded.get(row[3], 0) + int(row[15])

    def get_total_corners(self, row):
        # Total corners team
        self.team_total_corners[row[2]] = self.team_total_corners.get(row[2], 0) + int(row[17])
        self.team_total_corners[row[3]] = self.team_total_corners.get(row[3], 0) + int(row[18])
        # Total corners home / away
        self.home_team_total_corners[row[2]] = self.home_team_total_corners.get(row[2], 0) + int(row[17])
        self.away_team_total_corners[row[3]] = self.away_team_total_corners.get(row[3], 0) + int(row[18])
        # Total corners team conceded
        self.team_total_corners_conceded[row[2]] = self.team_total_corners_conceded.get(row[2], 0) + int(row[18])
        self.team_total_corners_conceded[row[3]] = self.team_total_corners_conceded.get(row[3], 0) + int(row[17])
        # Total corners home / away conceded
        self.home_team_total_corners_conceded[row[2]] = self.home_team_total_corners_conceded.get(row[2], 0) + int(row[18])
        self.away_team_total_corners_conceded[row[3]] = self.away_team_total_corners_conceded.get(row[3], 0) + int(row[17])

    def get_total_cards(self, row):
        # Total yellow cards team
        self.team_total_yellow_cards[row[2]] = self.team_total_yellow_cards.get(row[2], 0) + int(row[19])
        self.team_total_yellow_cards[row[3]] = self.team_total_yellow_cards.get(row[3], 0) + int(row[20])
        # Total yellow cards home / away
        self.home_total_yellow_cards[row[2]] = self.home_total_yellow_cards.get(row[2], 0) + int(row[19])
        self.away_total_yellow_cards[row[3]] = self.away_total_yellow_cards.get(row[3], 0) + int(row[20])
        # Total yellow cards team conceded
        self.team_total_yellow_cards_conceded[row[2]] = self.team_total_yellow_cards_conceded.get(row[2], 0) + int(row[20])
        self.team_total_yellow_cards_conceded[row[3]] = self.team_total_yellow_cards_conceded.get(row[3], 0) + int(row[19])
        # Total yellow cards home / away conceded
        self.home_total_yellow_cards_conceded[row[2]] = self.home_total_yellow_cards_conceded.get(row[2], 0) + int(row[20])
        self.away_total_yellow_cards_conceded[row[3]] = self.away_total_yellow_cards_conceded.get(row[3], 0) + int(row[19])
        # Total red cards team
        self.team_total_red_cards[row[2]] = self.team_total_red_cards.get(row[2], 0) + int(row[21])
        self.team_total_red_cards[row[3]] = self.team_total_red_cards.get(row[3], 0) + int(row[22])
        # Total red cards home / away
        self.home_total_red_cards[row[2]] = self.home_total_red_cards.get(row[2], 0) + int(row[21])
        self.away_total_red_cards[row[3]] = self.away_total_red_cards.get(row[3], 0) + int(row[22])
        # Total red cards team conceded
        self.team_total_red_cards_conceded[row[2]] = self.team_total_red_cards_conceded.get(row[2], 0) + int(row[22])
        self.team_total_red_cards_conceded[row[3]] = self.team_total_red_cards_conceded.get(row[3], 0) + int(row[21])
        # Total red cards home / away conceded
        self.home_total_red_cards_conceded[row[2]] = self.home_total_red_cards_conceded.get(row[2], 0) + int(row[22])
        self.away_total_red_cards_conceded[row[3]] = self.away_total_red_cards_conceded.get(row[3], 0) + int(row[21])

    def get_or_create_total_stats(self, row, match):
        _, created = Totals.objects.get_or_create(
            match_id=match,
            home_team_total_goal_full_time=self.team_total_goal_full_time[row[2]],
            away_team_total_goal_full_time=self.team_total_goal_full_time[row[3]],
            home_team_total_goal_full_time_as_home=self.home_team_total_goal_full_time[row[2]],
            away_team_total_goal_full_time_as_away=self.away_team_total_goal_full_time[row[3]],
            home_team_total_goal_half_time=self.team_total_goal_half_time[row[2]],
            away_team_total_goal_half_time=self.team_total_goal_half_time[row[3]],
            home_team_total_goal_half_time_as_home=self.home_team_total_goal_half_time[row[2]],
            away_team_total_goal_half_time_as_away=self.away_team_total_goal_half_time[row[3]],
            home_team_total_goal_second_half_time=self.team_total_goal_full_time[row[2]]-self.team_total_goal_half_time[row[2]],
            away_team_total_goal_second_half_time=self.team_total_goal_full_time[row[3]]-self.team_total_goal_half_time[row[3]],
            home_team_total_goal_second_half_time_as_home=self.home_team_total_goal_full_time[row[2]]-self.home_team_total_goal_half_time[row[2]],
            away_team_total_goal_second_half_time_as_away=self.away_team_total_goal_full_time[row[3]]-self.away_team_total_goal_half_time[row[3]],
            home_team_total_goal_conceded_full_time=self.team_total_goal_conceded_full_time[row[2]],
            away_team_total_goal_conceded_full_time=self.team_total_goal_conceded_full_time[row[3]],
            home_team_total_goal_conceded_full_time_as_home=self.home_team_total_goal_conceded_full_time[row[2]],
            away_team_total_goal_conceded_full_time_as_away=self.away_team_total_goal_conceded_full_time[row[3]],
            home_team_total_goal_conceded_half_time=self.team_total_goal_conceded_half_time[row[2]],
            away_team_total_goal_conceded_half_time=self.team_total_goal_conceded_half_time[row[3]],
            home_team_total_goal_conceded_half_time_as_home=self.home_team_total_goal_conceded_half_time[row[2]],
            away_team_total_goal_conceded_half_time_as_away=self.away_team_total_goal_conceded_half_time[row[3]],
            home_team_total_goal_conceded_second_half_time=self.team_total_goal_conceded_full_time[row[2]]-self.team_total_goal_conceded_half_time[row[2]],
            away_team_total_goal_conceded_second_half_time=self.team_total_goal_conceded_full_time[row[3]]-self.team_total_goal_conceded_half_time[row[3]],
            home_team_total_goal_conceded_second_half_time_as_home=self.home_team_total_goal_conceded_full_time[row[2]]-self.home_team_total_goal_conceded_half_time[row[2]],
            away_team_total_goal_conceded_second_half_time_as_away=self.away_team_total_goal_conceded_full_time[row[3]]-self.away_team_total_goal_conceded_half_time[row[3]],
            home_team_total_shots=self.team_total_shots[row[2]],
            away_team_total_shots=self.team_total_shots[row[3]],
            home_team_total_shots_as_home=self.home_team_total_shots[row[2]],
            away_team_total_shots_as_away=self.away_team_total_shots[row[3]],
            home_team_total_shots_on_target=self.team_total_shots_on_target[row[2]],
            away_team_total_shots_on_target=self.team_total_shots_on_target[row[3]],
            home_team_total_shots_on_target_as_home=self.home_team_total_shots_on_target[row[2]],
            away_team_total_shots_on_target_as_away=self.away_team_total_shots_on_target[row[3]],
            home_team_total_shots_conceded=self.team_total_shots_conceded[row[2]],
            away_team_total_shots_conceded=self.team_total_shots_conceded[row[3]],
            home_team_total_shots_conceded_as_home=self.home_team_total_shots_conceded[row[2]],
            away_team_total_shots_conceded_as_away=self.away_team_total_shots_conceded[row[3]],
            home_team_total_shots_conceded_on_target=self.team_total_shots_conceded_on_target[row[2]],
            away_team_total_shots_conceded_on_target=self.team_total_shots_conceded_on_target[row[3]],
            home_team_total_shots_conceded_on_target_as_home=self.home_team_total_shots_conceded_on_target[row[2]],
            away_team_total_shots_conceded_on_target_as_away=self.away_team_total_shots_conceded_on_target[row[3]],
            home_team_total_fouls_commited=self.team_total_fouls_commited[row[2]],
            away_team_total_fouls_commited=self.team_total_fouls_commited[row[3]],
            home_team_total_fouls_commited_as_home=self.home_team_total_fouls_commited[row[2]],
            away_team_total_fouls_commited_as_away=self.away_team_total_fouls_commited[row[3]],
            home_team_total_fouls_conceded=self.team_total_fouls_conceded[row[2]],
            away_team_total_fouls_conceded=self.team_total_fouls_conceded[row[3]],
            home_team_total_fouls_conceded_as_home=self.home_team_total_fouls_conceded[row[2]],
            away_team_total_fouls_conceded_as_away=self.away_team_total_fouls_conceded[row[3]],
            home_team_total_corners=self.team_total_corners[row[2]],
            away_team_total_corners=self.team_total_corners[row[3]],
            home_team_total_corners_as_home=self.home_team_total_corners[row[2]],
            away_team_total_corners_as_away=self.away_team_total_corners[row[3]],
            home_team_total_corners_conceded=self.team_total_corners_conceded[row[2]],
            away_team_total_corners_conceded=self.team_total_corners_conceded[row[3]],
            home_team_total_corners_conceded_as_home=self.home_team_total_corners_conceded[row[2]],
            away_team_total_corners_conceded_as_away=self.away_team_total_corners_conceded[row[3]],
            home_team_total_yellow_cards=self.team_total_yellow_cards[row[2]],
            away_team_total_yellow_cards=self.team_total_yellow_cards[row[3]],
            home_team_total_yellow_cards_as_home=self.home_total_yellow_cards[row[2]],
            away_team_total_yellow_cards_as_away=self.away_total_yellow_cards[row[3]],
            home_team_total_yellow_cards_conceded=self.team_total_yellow_cards_conceded[row[2]],
            away_team_total_yellow_cards_conceded=self.team_total_yellow_cards_conceded[row[3]],
            home_team_total_yellow_cards_conceded_as_home=self.home_total_yellow_cards_conceded[row[2]],
            away_team_total_yellow_cards_conceded_as_away=self.away_total_yellow_cards_conceded[row[3]],
            home_team_total_red_cards=self.team_total_red_cards[row[2]],
            away_team_total_red_cards=self.team_total_red_cards[row[3]],
            home_team_total_red_cards_as_home=self.home_total_red_cards[row[2]],
            away_team_total_red_cards_as_away=self.away_total_red_cards[row[3]],
            home_team_total_red_cards_conceded=self.team_total_red_cards_conceded[row[2]],
            away_team_total_red_cards_conceded=self.team_total_red_cards_conceded[row[3]],
            home_team_total_red_cards_conceded_as_home=self.home_total_red_cards_conceded[row[2]],
            away_team_total_red_cards_conceded_as_away=self.away_total_red_cards_conceded[row[3]],
        )
