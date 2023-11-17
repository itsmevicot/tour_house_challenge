from django.core.management import BaseCommand, call_command
from authentication.models import BaseUser


class Command(BaseCommand):
    help = 'Command to load test data from fixtures of Employees, Companies and Departments.'

    def handle(self, *args, **kwargs):
        fixtures = ['companies.json', 'departments.json', 'employees.json']
        for fixture in fixtures:
            call_command('loaddata', fixture)

        if not BaseUser.objects.filter(email='admin@admin.com').exists():
            BaseUser.objects.create_superuser(
                email='admin@admin.com',
                password='admin'
            )
            print("Superuser created successfully!")

        print("Test data imported successfully!")
