def total_stats(pokemon_data):
    total = 0
    for stat in pokemon_data['stats']:
        total += stat['base_stat']
    return total