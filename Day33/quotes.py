import requests


response = requests.get("https://api.kanye.rest")
quotes = response.json()["quote"]
print(quotes)