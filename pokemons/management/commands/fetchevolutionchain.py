from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Fetch evolution chain from PokeApi'

    def add_arguments(self, parser):
        parser.add_argument('evolution_chain_id', type=int)

    def handle(self, *args, **options):
        print("ID passed to fetchevolutionchain command:", options['evolution_chain_id'])