from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Activate a user based on their email address'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email of the user to activate')

    def handle(self, *args, **options):
        email = options['email']
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                self.stdout.write(self.style.NOTICE(f'User {email} is already active.'))
                return
            if user.is_superuser:
                self.stdout.write(self.style.NOTICE(f'User {email} is a superuser and is already active.'))
                return
            user.is_active = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'User {email} has been successfully activated.'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User with email {email} does not exist.'))
