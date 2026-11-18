import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])
moves = open("./moves.json", encoding="utf8")
movedata = json.load(moves)


languages = ("japanese", "chinese", "english", "french")

while True:
    language = input("Choose your language (japanese, chinese, english, french): ").strip().lower()
    if language in languages:
        break
    print("That language is not in the list. Please try again.")


while True:
    selected_type = input("Enter a Pokemon type: ").strip().casefold()
    if not selected_type:
        print("Please enter a type.")
        continue

    matches = [
        pokemon
        for pokemon in pokedex
        if any(selected_type == kind.casefold() for kind in pokemon["type"])
    ]

    if not matches:
        print(f"No Pokemon found with the type '{selected_type}'.")
        continue

    for pokemon in matches:
        print(pokemon["name"][language])
    break


while True:
    selected_pokemon = input("Enter a Pokemon name: ").strip().casefold()
    if not selected_pokemon:
        print("Please enter a name.")
        continue

    matches = [
        pokemon
        for pokemon in pokedex
        if selected_pokemon in pokemon["name"][language].casefold()
    ]

    if not matches:
        print(f"No Pokemon found with the name '{selected_pokemon}'.")
        continue

    for pokemon in matches:
        print(pokemon["name"][language])
    break


while True:
    pokemon_selected = input("Enter a Pokemon name to see moves for its type: ").strip().casefold()
    if not pokemon_selected:
        print("Please enter a name.")
        continue

    pokemon_matches = [
        pokemon
        for pokemon in pokedex
        if pokemon_selected in pokemon["name"][language].casefold()
    ]

    if not pokemon_matches:
        print(f"No Pokemon found with the name '{pokemon_selected}'.")
        continue

    pokemon = next(
        (
            match
            for match in pokemon_matches
            if match["name"][language].casefold() == pokemon_selected
        ),
        pokemon_matches[0],
    )
    types = {kind.casefold() for kind in pokemon["type"]}
    matching_moves = [
        move
        for move in moves
        if move["type"].casefold() in types
    ]

    print(
        f"Moves matching {pokemon['name'][language]} "
        f"({', '.join(pokemon['type'])}):"
    )
    move_key = {
        "english": "ename",
        "japanese": "jname",
        "chinese": "cname",
    }.get(language, "ename")
    for move in matching_moves:
        print(move[move_key])
    break

