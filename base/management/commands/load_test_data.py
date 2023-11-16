from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Command to load test data from fixtures of Employees, Companies and Departments.'

    def handle(self, *args, **kwargs):
        fixtures = ['companies.json', 'departments.json', 'employees.json']

        for fixture in fixtures:
            call_command('loaddata', fixture)
        print("Test data imported successfully!")
