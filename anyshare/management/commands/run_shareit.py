from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run the Django development server on a specified port'

    def add_arguments(self, parser):
        parser.add_argument(
            '--port',
            type=int,
            nargs='?',
            default=8000,
            help='Port number to run the server on (default: 8000)',
        )
        parser.add_argument(
            '--deploy',
            type=str,
            nargs='?',
            default="",
            help='to get the deployment type',
        )
    def handle(self, *args, **kwargs):
        port = kwargs['port']
        deployment_type = kwargs['deploy']
        if deployment_type == 'local':
            self.stdout.write(self.style.SUCCESS(f'Starting server on port {port}...'))
            call_command('runserver', f'{port}')
        elif deployment_type == 'server':
            print("Server implementation yet to define")