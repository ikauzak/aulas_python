import requests

response = requests.get('https://www.google.com')

if response.status_code == 200:
    print('Site ok!')
elif response.status_code == 404:
    print('Página não encontrada!')
