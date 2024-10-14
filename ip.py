import requests
from prettytable import PrettyTable

def get_ip_info(ip_address):
    url = f'http://ip-api.com/json/{ip_address}'
    response = requests.get(url)
    return response.json()

def print_ip_info_pretty(ip_info):
    table = PrettyTable()
    table.field_names = ["Field", "Value"]
    for key, value in ip_info.items():
        table.add_row([key, value])
    print(table)

ip_info = get_ip_info('news.de')
print_ip_info_pretty(ip_info)