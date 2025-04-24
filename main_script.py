# Main code which pulls in battle_pokemon and the pick_pokemon modules
from pick_pokemon import user_picks_pokemon, pick_random_pokemon, user_pokemon_assignment
from battle_pokemon import battle
from fetch_pokemon_data import get_pokemon_data, output_pokemon_data

user_pokemon_data = get_pokemon_data(user_pokemon_assignment())
CPU_pokemon_data = get_pokemon_data(pick_random_pokemon())

print("\nYour pokemon:")
output_pokemon_data(user_pokemon_data)

print("\nCPU pokemon:")
output_pokemon_data(CPU_pokemon_data)

print("\n")
battle(user_pokemon_data, CPU_pokemon_data)