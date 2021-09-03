from requests import get


API_URL = 'https://pokeapi.co/api/v2/'


def request_poke_api(endpoint):
    try:
        response = get(API_URL + endpoint).json()
        return response

    except ConnectionError:
        return None
