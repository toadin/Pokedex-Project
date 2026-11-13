import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
languages = ("japanese", "chinese", "english","french")
language = input("Choose your langauge (japanese, chinese, english, french)")
if language not in languages:
    print("That language is not in the list. Please try again. ")
    input("Choose your langauge (japanese, chinese, english, french)")
else:
    for pokemon in data:
        print(pokemon["name"][language])

def find_pokemon_by_type(pokemon_list, selected_type):
    selected_type = selected_type.strip().casefold()

    return [
        pokemon
        for pokemon in pokemon_list
        if selected_type in (kind.casefold() for kind in pokemon["type"])
    ]
selected_type = input("Enter a Pokémon type: ").strip()

if selected_type:
    matches = find_pokemon_by_type(data, selected_type)

    if matches:
        for pokemon in matches:
            print(pokemon["name"][language])
    else:
        print(f"No Pokémon found with the type '{selected_type}'.")
        input("Enter a Pokémon type: ").strip()
        if selected_type:
            matches = find_pokemon_by_type(data, selected_type)

        if matches:
            for pokemon in matches:
                print(pokemon["name"][language])


