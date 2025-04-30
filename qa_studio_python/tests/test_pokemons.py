import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '19b227eaa532a00f6c07ba82c30f7df5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '28504'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Юрген Клопп'
