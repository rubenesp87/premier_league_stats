from django.core.management.base import BaseCommand
import csv
import os
from django.conf import settings
from football.models import Totals

CSV_PATH = os.path.join(settings.BASE_DIR, "football/output/data.csv")


class Command(BaseCommand):
    help = 'Export stats to a CSV'

    def handle(self, *args, **options):
        with open(CSV_PATH, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for obj in Totals.objects.all():
                row = []
                total_fields = self.get_model_fields(obj)
                row.append(obj.match_id.home_team)
                row.append(obj.match_id.away_team)
                row.append(obj.match_id.referee)
                row.append(obj.match_id.date.strftime("%d/%m/%Y"))
                row.append(obj.match_id.full_time_home_goals + obj.match_id.full_time_away_goals)
                for field in total_fields:
                    if str(field.name) in ('match_id', 'id'):
                        continue
                    row.append(getattr(obj, field.name))

                writer.writerow(row)

    def get_model_fields(self, model):
        return model._meta.fields
