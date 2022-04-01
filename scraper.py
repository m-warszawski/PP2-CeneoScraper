import requests

response = requests.get('https://www.ceneo.pl/105186036#tab=reviews_scroll')
print(response.text)
