import requests
import json
import random

def user_picks_pokemon() -> str:
    # Get the list of pokemon from the API
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    pokemon_list = json.loads(response.text)['results']

    for pokemon in pokemon_list:
        print(pokemon['name'])

    # Ask the user to choose a pokemon
    print('Enter your pokemon:')

    # Get the user's choice
    choice = input().lower()
    return choice

def pick_random_pokemon() -> str:
    # Get the list of pokemon from the API
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    pokemon_list = json.loads(response.text)['results']

    random_number = random.randrange(0,len(pokemon_list)-1)
    choice = pokemon_list[random_number]["name"]
    return choice
