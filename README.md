# RIPE Information Lookup Tool

This Python script allows you to retrieve detailed information about an IP address or domain name using the RIPEstat API. The script can handle both IP addresses and domain names, resolving the domain to an IP address if necessary.

## Features

- **IP and Domain Lookup**: Retrieve detailed information about an IP address or domain name.
- **RIPEstat API Integration**: Utilizes the RIPEstat API to fetch comprehensive data.
- **Pretty Output**: Displays the retrieved information in a readable table format using `PrettyTable`.

## Requirements

- Python 3.6 or higher
- `requests` library
- `prettytable` library

You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```


Run the script

```bash
python3 ip.py 8.8.8.8
```
or
```bash
python3 ip.py google.com
```