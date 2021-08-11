#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    """Run time code"""

    resp = requests.get(f"{API}sets")
    print( resp.json())

if __name__ == "__main__":
    main()
