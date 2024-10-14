import requests
from prettytable import PrettyTable
import argparse
import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def get_ripe_info(ip_address):
    url = f'https://stat.ripe.net/data/whois/data.json?resource={ip_address}'
    response = requests.get(url)
    return response.json()

def print_ripe_info_pretty(ripe_info):
    table = PrettyTable()
    table.field_names = ["Field", "Value"]

    data = ripe_info.get('data', {}).get('records', [])
    for record in data:
        for item in record:
            table.add_row([item.get('key', ''), item.get('value', '')])

    print(table)

def main():
    parser = argparse.ArgumentParser(description="Get RIPE information")
    parser.add_argument("query", help="IP address or domain name to lookup")
    args = parser.parse_args()

    try:
        socket.inet_aton(args.query)
        ip_address = args.query
    except socket.error:
        ip_address = get_ip_address(args.query)
        if ip_address is None:
            print(f"Could not resolve domain: {args.query}")
            return

    print(f"\nRIPE Information for {ip_address}:")
    ripe_info = get_ripe_info(ip_address)
    print_ripe_info_pretty(ripe_info)

if __name__ == "__main__":
    main()