# your_project/management/commands/create_superuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError
import sys

class Command(BaseCommand):
    help = 'Creates a superuser with a given username and password'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Superuser username')
        parser.add_argument('--password', type=str, help='Superuser password')
        parser.add_argument('--email', type=str, help='Superuser email')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        email = kwargs['email']

        if not username or not password or not email:
            self.stderr.write(self.style.ERROR('You must provide a username, password, and email.'))
            sys.exit(1)

        try:
            user = User.objects.create_superuser(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully!'))
        except IntegrityError:
            self.stderr.write(self.style.WARNING(f'Superuser {username} already exists.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {str(e)}'))
            sys.exit(1)