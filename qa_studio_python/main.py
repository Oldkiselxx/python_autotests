import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '19b227eaa532a00f6c07ba82c30f7df5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '28504'

body_create = {
    "name": "Наруто",
    "photo_id": 5
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change_name = {
    "pokemon_id": pokemon_id,
    "name": "Саске",
    "photo_id": 5
}

response_change_name = requests.put(url =f'{URL}/pokemons', headers = HEADER, json = body_change_name)  
print(response_change_name.text)

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)