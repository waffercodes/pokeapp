from django.db import models

from .utils import request_poke_api


class EvolutionChain(models.Model):
    id = models.IntegerField(primary_key=True)
    pokemon = models.ForeignKey(
        'Pokemon', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.pokemon.name + " Evolution Chain"

    def __eq__(self, ev_chain):
        return self.id == ev_chain.id


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    base_stats = models.JSONField()

    evolves_to = models.ForeignKey(
        'Pokemon', on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name

    def __eq__(self, pokemon):
        return self.id == pokemon.id
    
    def set_evolves_to(self, some_pokemon):
        self.evolves_to = some_pokemon
        self.save()

    @classmethod
    def fetch_from_poke_api_by_name(cls, pokemon_name):

        # Search for Pokemon, if it is registered there's no need to register it again
        pokemon = cls.objects.filter(name=pokemon_name)

        if pokemon:
            return None

        endpoint = 'pokemon/%s' % pokemon_name
        pokemon_json = request_poke_api(endpoint)

        return cls(
            id=pokemon_json['id'],
            name=pokemon_json['name'],
            height=pokemon_json['height'],
            weight=pokemon_json['weight'],
            base_stats=pokemon_json['stats']
        )
