from api_client import get_pokemon
from file_writer import save_json


def main():
    # Define the pokemon name
    pokemon_name = "pikachu"

    # Fetch data from PokeAPI
    pokemon = get_pokemon(pokemon_name)

    # Save raw API response as JSON
    output_path = f"data/raw/pokemon_{pokemon_name}.json"
    save_json(pokemon, output_path)

    # Display main fields from the response
    print(f"Name: {pokemon['name']}")
    print(f"ID: {pokemon['id']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")


if __name__ == "__main__":
    main()