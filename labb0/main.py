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
player_attack = ""
player_type = ""
player_hp = ""

opponent_pokemon = ""
opponent_hp = ""
opponent_attack =  ""
opponent_type = ""


def main():
    print("-"*40)
    print("Welcome to a LIDL pokemon game")
    print("-"*40)
    while True:
        menu()
        choice = input("Ange val: ")
        if choice == "1":
            fight()
        if choice == "2":
            choose_pokemon()
        elif choice == "0":
            print("*" * 40)
            print("Good game!")
            print("*" * 40)
            exit()
        print("\n")


def menu():
    print("1. Duel")
    print("2. Switch Pokemon")
    print("3. Quit")

def choose_pokemon():
    user_pokemon = input("Which Pokemon do you want to use?")
    if user_pokemon in pokemons:
        chosen_pokemon = pokemons[user_pokemon]
        global player_pokemon
        player_pokemon = user_pokemon
        global player_hp
        player_hp = chosen_pokemon["hp"] * random.uniform(0.5, 1.5)
        global player_attack
        player_attack = chosen_pokemon["damage"]
        global player_type
        player_type = chosen_pokemon["type"] 
        print(player_attack, player_hp, player_pokemon, player_type)

    else:
        print("There is no pokemon with this name")


def fight():
    random_opponent_pokemon()
    global opponent_hp
    opponent_hp = opponent_hp
    global player_hp
    player_hp = player_hp
    if player_pokemon == "":
        print("You need to select a pokemon!")
        choose_pokemon()
    else:
        print(player_pokemon, ", I Choose you!")
        print(opponent_pokemon, ",get him!")
        first_attack = random.randint(1,2)
        if first_attack == 1:
            opponent_hp -= player_attack
        else:
            player_hp -= opponent_attack
        while opponent_hp or player_hp is not 0:
            if opponent_hp <= 0:
                print("Congratulations,", player_pokemon, "recieved 42 experience for winning!")
                break
            elif player_hp <= 0:
                print("You lost!")
                break
            opponent_hp -= round(player_attack * (random.uniform(0.5, 1.5)))
            print(player_pokemon, "attacks", opponent_pokemon, "for", round(player_attack * (random.uniform(0.5, 1.5))), "damage")
            print("The Player has", round(player_hp), "health and the opponent has", round(opponent_hp), "left!")
            time.sleep(0.5)
            player_hp -= round(opponent_attack * random.uniform(0.5, 1.5))
            print(opponent_pokemon, "attacks", player_pokemon, "for", round(opponent_attack * (random.uniform(0.5, 1.5))), "damage")
            print("The Player has", round(player_hp), "health and the opponent has", round(opponent_hp), "left!")
            time.sleep(0.5)
            

def random_opponent_pokemon():
    pokemon_stats = list(pokemons.keys())
    choose_opponent_pokemon = random.choice(pokemon_stats)
    global opponent_pokemon
    opponent_pokemon = pokemons[choose_opponent_pokemon]
    global opponent_hp
    opponent_hp = opponent_pokemon["hp"] * random.uniform(0.5, 1.5)
    global opponent_attack
    opponent_attack =  opponent_pokemon["damage"]
    global opponent_type
    opponent_type = opponent_pokemon["type"]

main()