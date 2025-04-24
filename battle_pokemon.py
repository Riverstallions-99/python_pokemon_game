def total_stats(pokemon_data):
    total = 0
    for stat in pokemon_data['stats']:
        print(stat['base_stat'])
        total += stat['base_stat']
    return total

def battle(user_pokemon_data, cpu_pokemon_data):
    if total_stats(user_pokemon_data) > total_stats(cpu_pokemon_data):
        print("User pokemon won")
    elif total_stats(user_pokemon_data) < total_stats(cpu_pokemon_data):
        print("CPU pokemon won")
    else:
        print("Tie / Draw!")