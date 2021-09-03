from rest_framework.views import APIView
from rest_framework.response import Response

from pokemons.models import Pokemon, EvolutionChain
from pokemons.serializers import PokemonSerializer


class PokemonSearchAPIView(APIView):
    """
    Search Pokemon by name web service
    """

    def get(self, request, *args, **kwargs):
        pokemon_name = request.query_params.get('pokemon_name', None)

        pokemons = Pokemon.objects.filter(
            name__icontains=pokemon_name
        )
        pokemons_serialized = PokemonSerializer(pokemons, many=True)

        return Response(pokemons_serialized.data)