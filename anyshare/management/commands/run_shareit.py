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
            '--local',
            type=str,
            nargs='?',
            default="",
            help='to get the deployment type',
        )        
        parser.add_argument(
            '--server',
            type=str,
            nargs='?',
            default="",
            help='to get the deployment type',
        )        
    def handle(self, *args, **kwargs):
        port = kwargs['port']
        if kwargs.get('local') is None:  
            self.stdout.write(self.style.SUCCESS(f'Starting server on port {port}...'))
            call_command('runserver', f'{port}')
        else:
            print("Server implementation yet to define")