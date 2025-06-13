import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_animals_data(animals_data):
    for animal in animals_data:
        name = animal.get("name")
        taxonomy = animal.get("taxonomy")
        order = taxonomy.get("order")
        locations = animal.get("locations")
        typ = animal.get("type")

        if name:
            print(f"Name: {name}")
        if order:
            print(f"Diet: {order}")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")
        if typ:
            print(f"Type: {typ}")
        print()


def main():
    animals_data = load_data('animals_data.json')
    read_animals_data(animals_data)


if __name__ == "__main__":
    main()




