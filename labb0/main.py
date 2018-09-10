import time
import random

pokemons = [
    {
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
]



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
    for pokemon in pokemons:
        if user_pokemon is pokemon:
            return user_pokemon
        else:
            print("There is no pokemon with this name")




main()