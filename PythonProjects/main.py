import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '616cbfa52227263a76d870b4adb8548c'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

create_body = {
    "name": "Гудвин",
    "photo_id": 522
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_body)
print(response_create.text)

pokemon_id = response_create.json()['id']

change_body = {
    "pokemon_id": '173909',
    "name": "Зубастик",
    "photo_id": 521
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_body)
print(response_change.text)


pokeball_body = {
    "pokemon_id": '173909'
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokeball_body)
print(response_pokeball.text)

