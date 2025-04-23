# Main code which pulls in battle_pokemon and the pick_pokemon modules
from pick_pokemon import user_picks_pokemon, CPU_picks_random_pokemon
import requests, json, random

CPU_pokemon = CPU_picks_random_pokemon()
assign_player_random_pokemon = input("Would you like to:\n1. Choose your own pokemon\n2. Get assigned a random pokemon\nEnter 1 or 2: ")
user_pokemon = user_picks_pokemon()

def get_pokemon_data(pokemon_name:str) -> dict:
    # Get the pokemon's data from the API
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)
    response = requests.get(url)
    pokemon_data = json.loads(response.text)
    return pokemon_data

user_pokemon_data = get_pokemon_data(user_pokemon)
CPU_pokemon_data = get_pokemon_data(CPU_pokemon)

# Print the pokemon's data
def output_pokemon_data(pokemon_data):
    # to get ability
    abilities = user_pokemon_data['abilities'][0]
    ability = abilities['ability']

    # to format height and weight properly
    height = int(pokemon_data['height'])
    weight = int(pokemon_data['weight'])
    height_formatted = height / 10
    weight_formatted = weight / 10

    print('Name: {}'.format(pokemon_data['name']))
    print('Weight: {}'.format(weight_formatted) + "(kgs)")
    print('Height: {}'.format(height_formatted) + "(m)")
    print('Ability: {}'.format(ability['name']))

output_pokemon_data(user_pokemon_data)
