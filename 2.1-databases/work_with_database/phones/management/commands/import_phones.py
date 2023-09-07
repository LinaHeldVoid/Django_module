import csv

from django.core.management.base import BaseCommand, CommandError
from work_with_database.phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('phones.csv', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['phones.csv']:
            data_reader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            for row in data_reader:
                name = row[1]
                photo = row[2]
                price = row[3]
                release_date = row[4]
                lte_exists = row[5]
