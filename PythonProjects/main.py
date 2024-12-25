import requests

# {'id': '12181', 'trainer_token': '616cbfa52227263a76d870b4adb8548c', 'trainer_name': 'Tasha'}

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '616cbfa52227263a76d870b4adb8548c'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

create_body = {
    "name": "Говорун",
    "photo_id": 521
}

change_body = {
    "pokemon_id": "160067",
    "name": "Зубастик",
    "photo_id": 521
}

pokeball_body = {
    "pokemon_id": "160067"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_body)
print(response_create.text)


response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_body)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokeball_body)
print(response_pokeball.text)