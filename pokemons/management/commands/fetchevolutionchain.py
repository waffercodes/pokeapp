from pprint import pprint

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError

from pokemons.models import EvolutionChain, Pokemon
from pokemons.utils import request_poke_api


class Command(BaseCommand):
    help = 'Fetch Evolution Chain from PokeApi'

    def add_arguments(self, parser):
        parser.add_argument('evolution_chain_id', type=int)

    def handle(self, *args, **options):
        evolution_chain_id = options['evolution_chain_id']

        evolution_chain = EvolutionChain.objects.filter(
            id=evolution_chain_id
        )

        if evolution_chain:
            print("Evolution chain is already registered. Try another one.")
            return

        endpoint = 'evolution-chain/%s' % evolution_chain_id

        evolution_chain_json = request_poke_api(endpoint)

        if evolution_chain_json is None:
            print("A Connection Error occurred. Check your connection and try again.")
            return
        evolutions = []
        try:
            # Assert the Evolution Chain ID is the same we're looking for
            assert options['evolution_chain_id'] == evolution_chain_json['id']

            # Store first Pokemon
            evolution_chain_json = evolution_chain_json['chain']
            pokemon_name = evolution_chain_json['species']['name']
            pokemon = Pokemon.fetch_from_poke_api_by_name(pokemon_name)

            if pokemon is None:
                print(
                    f"Pokemon with name {evolution_chain_json['species']['name']} is already registered")
                return

            pokemon.save()
            print(f"Saved Pokemon {pokemon.name} with {pokemon.id} ID")

            evolution_chain = EvolutionChain(
                id=options['evolution_chain_id'],
                pokemon=pokemon
            )

            evolution_chain.save()
            print(
                f"Saved evolution chain for {pokemon.name.title()} with {evolution_chain.id} ID")

            # Save the rest of the chain on Pokemon's evolves_to field
            while 'evolves_to' in evolution_chain_json.keys() and evolution_chain_json['evolves_to']:
                evolution_chain_json = evolution_chain_json['evolves_to'][0]
                next_pokemon = Pokemon.fetch_from_poke_api_by_name(
                    evolution_chain_json['species']['name']
                )

                if next_pokemon is not None:
                    next_pokemon.save()

                    pokemon.set_evolves_to(next_pokemon)
                    print(f"Added Pokemon {pokemon.name} with {pokemon.id} to Evolution Chain")

                    pokemon = next_pokemon

        except ValidationError as e:
            print("Validation Errors were found: ", ', '.join(e.errors))
            return

        except AssertionError as e:
            print("ID specified doesn't match the ID retrieved from API")
            return

        except Exception as e:
            print(f"Something odd happened: {e}")
            return
