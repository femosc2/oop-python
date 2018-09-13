import time
import random

pokemons = {
    "Charmander": {
        "type": "fire",
        "damage": 15,
        "hp": 75,
        "weakness": "water"
    },
    "Bulbasaur": {
        "type": "grass",
        "damage": 12,
        "hp": 87,
        "weakness": "fire"
    },
    "Squirtle": {
        "type": "water",
        "damage": 13,
        "hp": 79,
        "weakness": "electric"
    },
    "Pikachu": {
        "type": "electric",
        "damage": 18,
        "hp": 68,
        "weakness": "grass"
    }
}


player_pokemon = ""
player_pokemon_name = ""
player_attack = ""
player_type = ""
player_hp = ""

opponent_pokemon = ""
opponent_pokemon_name = ""
opponent_hp = ""
opponent_attack =  ""
opponent_type = ""

wins = 0
losses = 0


def main():
    print("-"*40)
    print("Welcome to a LIDL pokemon game")
    print("-"*40)
    starter_pokemon()
    while True:
        menu()
        choice = input("Choose 1 to duel, 2 to choose pokemon, 3 to see statistics and 0 to exit the application!")
        if choice == "1":
            fight()
        if choice == "2":
            choose_pokemon()
        if choice == "3":
            show_statistics()
        elif choice == "0":
            print("-" * 40)
            print("Good game!")
            print("-" * 40)
            exit()
        print("\n")


def menu():
    print("1. Duel")
    print("2. Choose Pokemon")
    print("3. Show Statistics")
    print("0. Quit")

def choose_pokemon():
    for pokemon in pokemons:
        print(pokemon)
    user_pokemon = input("Which Pokemon do you want to use?").capitalize()
    if user_pokemon in pokemons:
        chosen_pokemon = pokemons[user_pokemon]
        global player_pokemon
        player_pokemon = user_pokemon
        global player_pokemon_name
        player_pokemon_name = user_pokemon
        global player_hp
        player_hp = chosen_pokemon["hp"] * random.uniform(0.5, 1.5)
        global player_attack
        player_attack = chosen_pokemon["damage"]
        global player_type
        player_type = chosen_pokemon["type"] 

    else:
        print("There is no pokemon with this name!")
        print("Please choose one of the following Pokemons!")


def fight():
    global losses
    global wins

    random_opponent_pokemon()

    temp_opp_hp = opponent_hp
    temp_player_hp = player_hp
    temp_opponent_attack = opponent_attack
    temp_player_attack = player_attack
    
    calculate_weakness()

    if player_pokemon == "":
        print("You need to choose a pokemon!")
        choose_pokemon()
    else: 
        print(player_pokemon, ", I Choose you!")
        print(opponent_pokemon_name, ",get him!")

        first_attack = random.randint(1,2)
        if first_attack == 1:
            temp_opp_hp -= temp_player_attack
            print(player_pokemon_name, "attacks", opponent_pokemon_name, "for", round(temp_player_attack * (random.uniform(0.5, 1.5))), "damage")
            print("The Player has", round(temp_player_hp), "health and the opponent has", round(temp_opp_hp), "left!")
        else:
            temp_player_hp -= temp_opponent_attack
            print(opponent_pokemon_name, "attacks", player_pokemon_name, "for", round(temp_opponent_attack * (random.uniform(0.5, 1.5))), "damage")
            print("The Player has", round(temp_player_hp), "health and the opponent has", round(temp_opp_hp), "left!")

        while temp_opp_hp or temp_player_hp >= 0:
            temp_opp_hp -= round(temp_player_attack * (random.uniform(0.5, 1.5)))
            print(player_pokemon_name, "attacks", opponent_pokemon_name, "for", round(temp_player_attack * (random.uniform(0.5, 1.5))), "damage")

            if temp_opp_hp <= 0:
                print("Congratulations,", player_pokemon_name, "recieved", random.randint(0,99), "experience for winning!")
                wins += 1
                break
            print("The Player has", round(temp_player_hp), "health and the opponent has", round(temp_opp_hp), "left!")

            time.sleep(1)

            temp_player_hp -= round(temp_opponent_attack * random.uniform(0.5, 1.5))
            print(opponent_pokemon_name, "attacks", player_pokemon_name, "for", round(temp_opponent_attack * (random.uniform(0.5, 1.5))), "damage")
            print("The Player has", round(temp_player_hp), "health and the opponent has", round(temp_opp_hp), "left!")

            if temp_player_hp <= 0:
                print("You lost!")
                losses += 1
                break
            time.sleep(1)
            

def random_opponent_pokemon():
    pokemon_stats = list(pokemons.keys())
    choose_opponent_pokemon = random.choice(pokemon_stats)
    global opponent_pokemon
    opponent_pokemon = pokemons[choose_opponent_pokemon]
    global opponent_pokemon_name
    opponent_pokemon_name = choose_opponent_pokemon
    print(opponent_pokemon_name)
    global opponent_hp
    opponent_hp = opponent_pokemon["hp"] * random.uniform(0.5, 1.5)
    global opponent_attack
    opponent_attack =  opponent_pokemon["damage"]
    global opponent_type
    opponent_type = opponent_pokemon["type"]

def show_statistics():
    print("You have won", wins, "times and lost", losses, "times!")


def calculate_weakness():
    global player_attack
    global opponent_attack
    temp_player_attack = player_attack
    temp_opponent_attack = opponent_attack
    if player_type == "fire" and opponent_type == "grass":
        temp_player_attack *= 1.25
    elif opponent_type == "fire" and player_type == "grass":
        temp_opponent_attack *= 1.25
    elif player_type == "water" and opponent_type == "fire":
        temp_player_attack *= 1.25
    elif opponent_type == "water" and player_type == "fire":
        temp_opponent_attack *= 1.25
    elif player_type == "electric" and opponent_type == "water":
        temp_player_attack *= 1.25
    elif opponent_type == "electric" and opponent_type == "water":
        temp_opponent_attack *= 1.25
    elif player_type == "grass" and opponent_type == "electric":
        temp_player_attack *= 1.25
    elif opponent_type == "grass" and player_type == "electric":
        temp_opponent_attack *= 1.25

def starter_pokemon():
    print("Welcome to the world of Pokemon! You've been given a choice of four pokemons! Which one do you choose as a starter?")
    while player_pokemon == "":
        choose_pokemon()
    choose_name = input("What do you want to name your starter pokemon?")
    global player_pokemon_name
    player_pokemon_name = choose_name
        


main()