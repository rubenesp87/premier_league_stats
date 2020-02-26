from football.models import Referee


def add_stats_to_referee(referee, row):
    referee.home_yellow_cards += int(row[19])
    referee.away_yellow_cards += int(row[20])
    referee.home_red_cards += int(row[21])
    referee.away_red_cards += int(row[22])
    referee.num_matches += 1
    referee.save()


def get_or_create_referee_stats(row):
    defaults = dict(
        home_yellow_cards=row[19],
        away_yellow_cards=row[20],
        home_red_cards=row[21],
        away_red_cards=row[22],
        num_matches=1,
    )

    referee, referee_created = Referee.objects.get_or_create(
        name=row[10],
        defaults=defaults,
    )

    if not referee_created:
        add_stats_to_referee(referee, row)
