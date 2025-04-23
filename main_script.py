# Main code which pulls in battle_pokemon and the pick_pokemon modules
from pick_pokemon import user_picks_pokemon, CPU_picks_random_pokemon
import requests, json, random

CPU_pokemon = CPU_picks_random_pokemon()
user_pokemon = user_picks_pokemon()

def get_pokemon_data(pokemon_name:str) -> dict:
    # Get the pokemon's data from the API
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)
    response = requests.get(url)
    pokemon_data = json.loads(response.text)
    return pokemon_data

user_pokemon_data = get_pokemon_data(user_pokemon)
CPU_pokemon_data = get_pokemon_data(CPU_pokemon)

# to get ability
abilities = user_pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(user_pokemon_data['height'])
weight = int(user_pokemon_data['weight'])
height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
def output_pokemon_data():
    print('Name: {}'.format(user_pokemon_data['name']))
    print('Weight: {}'.format(weight_formatted) + "(kgs)")
    print('Height: {}'.format(height_formatted) + "(m)")
    print('Ability: {}'.format(ability['name']))