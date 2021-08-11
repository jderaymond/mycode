#!/usr/bin/env python3
import requests

def main():
    """Run time code"""

    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    print( dir(resp) )

if __name__ == "__main__":
    main()
