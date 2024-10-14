import requests

def get_as_info(as_number):
    url = f'https://stat.ripe.net/data/as-overview/data.json?resource=AS{as_number}'
    response = requests.get(url)
    return response.json()

as_info = get_as_info('15169')  # Пример AS 15169 (Google LLC)
print(as_info)