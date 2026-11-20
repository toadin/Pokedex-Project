import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])
moves = open("./moves.json", encoding="utf8")
movedata = json.load(moves)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
languages = ("japanese", "chinese", "english","french")
while True:
    language = input("Choose your language (japanese, chinese, english, french)").strip().lower()
    if language in languages:
        break
    else:
        print("That language is not in the list. Please try again.")

while True:
    selected_type = input("Enter a Pokémon type: ").strip().casefold()
    if not selected_type:
        print("Please enter a type.")
        continue

    matches = [
        pokemon
        for pokemon in data
        if any(selected_type == kind.casefold() for kind in pokemon["type"])
    ]

    if not matches:
        print(f"No Pokémon found with the type '{selected_type}'.")
        continue

    for pokemon in matches:
        print(pokemon["name"][language])
    break

while True:
    selected_pokemon = input("Enter a Pokémon name: ").strip().casefold()
    if not selected_pokemon:
        print("Please enter a name.")
        continue

    matches = [
        pokemon
        for pokemon in data
        if selected_pokemon in pokemon["name"][language].casefold()
    ]

    if not matches:
        print(f"No Pokémon found with the name '{selected_pokemon}'.")
        continue 

    for pokemon in matches:
        print(pokemon["name"][language])
    break

while True:
    pokemon_selected = input("Enter a Pokémon name for which you would like to know the moves: ").strip().casefold()
    if not pokemon_selected:
        print("Please enter a name.")
        continue

    matches = [
        pokemon
        for pokemon in data
        if pokemon_selected in pokemon["name"][language].casefold()
    ]

    if not matches:
        print(f"This is not one of the '{selected_pokemon}'.")
        continue

    for pokemon in matches:
        print(pokemon["name"][language])
        for move in movedata:
            if move["type"] in pokemon["type"]:
                print(move["ename"])
    break

