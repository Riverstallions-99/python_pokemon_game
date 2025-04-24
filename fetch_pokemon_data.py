import requests, json

def get_pokemon_data(pokemon_name:str) -> dict:
    # Get the pokemon's data from the API
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)
    response = requests.get(url)
    pokemon_data = json.loads(response.text)
    return pokemon_data

# Print the pokemon's data
def output_pokemon_data(pokemon_data):
    # to get ability
    abilities = pokemon_data['abilities'][0]
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