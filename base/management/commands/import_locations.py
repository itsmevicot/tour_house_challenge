import csv
import time
from django.core.management.base import BaseCommand
from django.db import transaction
from base.models import Country, State, City


class Command(BaseCommand):
    help = 'Import countries, states, and cities from CSV'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.import_countries()
            self.import_states()
            self.import_cities()

    def import_countries(self):
        start_time = time.time()
        print("Starting import of countries...")
        with open('base/fixtures/countries.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            countries = [Country(id=row['id'], name=row['name'], iso3=row['iso3']) for row in reader]
            Country.objects.bulk_create(countries)
        print(f"Completed import of countries in {time.time() - start_time:.2f} seconds.")

    def import_states(self):
        start_time = time.time()
        print("Starting import of states...")
        with open('base/fixtures/states.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            country_mapping = {country.id: country for country in Country.objects.all()}
            states = []
            for row in reader:
                country = country_mapping.get(int(row['country_id']))
                if country:
                    states.append(State(id=row['id'], name=row['name'], country=country))
            State.objects.bulk_create(states)
        print(f"Completed import of states in {time.time() - start_time:.2f} seconds.")

    def import_cities(self):
        start_time = time.time()
        print("Starting import of cities...")
        with open('base/fixtures/cities.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            state_mapping = {state.id: state for state in State.objects.all()}
            cities = []
            for row in reader:
                state = state_mapping.get(int(row['state_id']))
                if state:
                    cities.append(City(id=row['id'], name=row['name'], state=state, state_code=row['state_code']))
            City.objects.bulk_create(cities)
        print(f"Completed import of cities in {time.time() - start_time:.2f} seconds.")
