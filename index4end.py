import random

def generate_doors(num_doors, num_prizes):
    doors = ["пусто"] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for idx in prize_indices:
        doors[idx] = "приз"
    return doors

def simulate_game(num_doors, num_prizes):
    doors = generate_doors(num_doors, num_prizes)
    player_choice = random.randint(0, num_doors - 1)
    # Открываем одну из дверей, за которой нет приза
    revealed_door = random.choice([idx for idx in range(num_doors) if idx != player_choice and doors[idx] == "пусто"])
    # Игрок решает изменить выбор
    player_choice_new = random.choice([idx for idx in range(num_doors) if idx != player_choice and idx != revealed_door])
    # Возвращаем результаты: True, если игрок выиграл, иначе False
    return doors[player_choice_new] == "приз", doors[player_choice] == "приз"

# Пример использования
num_doors = 3
num_prizes = 1
num_simulations = 10000

switch_wins = 0
stay_wins = 0
for _ in range(num_simulations):
    switch_win, stay_win = simulate_game(num_doors, num_prizes)
    if switch_win:
        switch_wins += 1
    if stay_win:
        stay_wins += 1

switch_win_probability = switch_wins / num_simulations
stay_win_probability = stay_wins / num_simulations

