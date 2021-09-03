from django.db.models.base import Model
from rest_framework import serializers

from .models import Pokemon, EvolutionChain


class EvolutionChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvolutionChain
        fields = ['id', 'pokemon']


class PokemonSerializer(serializers.ModelSerializer):
    evolves_to = serializers.SerializerMethodField()
    class Meta:
        model = Pokemon
        fields = '__all__'

    def get_evolves_to(self, obj):
        if obj.evolves_to:
            evol_pokemon = Pokemon.objects.get(id=obj.evolves_to.id)
            serializer = PokemonSerializer(evol_pokemon)
            return serializer.data
        return None