import requests
import json
import random

def user_pokemon_assignment() -> str:
    user_prompt = True
    while user_prompt:
        assign_player_random_pokemon = input("Would you like to:\n1. Choose your own pokemon\n2. Get assigned a random pokemon\nEnter 1 or 2: ")
        if assign_player_random_pokemon.isdigit() and (int(assign_player_random_pokemon) == 1 or int(assign_player_random_pokemon) == 2):
            user_prompt = False
            assign_player_random_pokemon = bool(int(assign_player_random_pokemon)-1)
        else:
            print("Invalid input.")

    if assign_player_random_pokemon:
        user_pokemon = pick_random_pokemon()
    else:
        user_pokemon = user_picks_pokemon()
    return user_pokemon
            
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
