from django.core.management.base import BaseCommand
from football.models import (
    Match,
    Referee,
    Totals,
)
import pprint


class Command(BaseCommand):
    help = 'Show DB data'

    def handle(self, *args, **options):
        # Totals.objects.all().delete()
        # Referee.objects.all().delete()
        # Match.objects.all().delete()

        match = Match.objects.all()
        pp = pprint.PrettyPrinter(indent=4)
        for data in match:
            pp.pprint(data.__dict__)

        totals = Totals.objects.order_by("id")[:2]
        pp = pprint.PrettyPrinter(indent=4)
        for data in totals:
            pp.pprint(data.__dict__)

        referee = Referee.objects.order_by("id")[:2]
        pp = pprint.PrettyPrinter(indent=4)
        for data in referee:
            pp.pprint(data.__dict__)
