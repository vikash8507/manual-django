import os
from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):

    def add_arguments(self, parser):
        parser.add_argument('--db', dest='postgres_use', default=1)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        if options.get('postgres_use') == '1':
            os.environ['postgres_use'] = 'yes'
        else:
            os.environ['postgres_use'] = 'no'
        super(Command, self).handle(*args, **options)
    