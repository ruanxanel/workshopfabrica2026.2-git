import requests

nome_pokemon = input("Digite o nome do Pokémon: ")

resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}")

dados = resposta.json()


print(dados["name"])
print(dados["height"])
print(dados["weight"])
print(dados["types"][0]["type"]["name"])