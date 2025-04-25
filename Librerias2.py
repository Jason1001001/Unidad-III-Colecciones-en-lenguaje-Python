import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"
pokemon = input ("ingrese su pokemon: ")
urlCompleta = url + pokemon

resultado = requests.get(urlCompleta)

diccionarioPokemon = resultado.json()
print("Bienvenido a la pokedex: ")
print("Nombre del pokemon: ")
print(diccionarioPokemon["forms"][0]["url"])
print("Hablidades: ")
print(diccionarioPokemon["abilities"][0]["name"])
print(diccionarioPokemon["abilities"][1]["name"])