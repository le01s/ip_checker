import requests

def get_ip_info(ip_address):
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url)
    return response.json()

ip_info = get_ip_info('8.8.8.8')
print(ip_info)