# PokeApp Technical Test

## Description

A Pokemon is a mystical creature that belongs to a fictional world, designed
and managed by the Japanese companies Nintendo, Game Freak and
Creatures. The Pokemon world is available on manga, anime adaptions, games,
retail stores and many more places.
The depth of this virtual world allows to have mountains of data only to describe
completely a Pokemon and its relations around the universe. This information is
available on the PokeApi (https://pokeapi.co/docs/v2.html).

## Purpose

The purpose of this Django App is to fetch information about the Pokemons and its Evolution Chains
using a custom Django command and exposing as well an API Endpoint to search the Pokemons fetched before 
using the Django command

## How to run it

* Clone the repo
* Navigate the repo folder
* Create a Python virtualenv in your favorite way
* Run

```
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver <some-port>
```

## Fetch Pokemon information and Evolution Chains

Run

```
python manage.py fetchevolutionchain <int:some_id>
```

In order to fetch Pokemon Evolution Chain with the given ID and store all of its Pokemons in the DB


## Search service

Make a GET request to the ```/pokemons/search?pokemon_name=somename``` with pokemon_name as a query parameter to retrieve a list of matching Pokemons 
