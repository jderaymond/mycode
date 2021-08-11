#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        resp = requests.get(AOIF_CHAR + got_charToLookup).json()

        allies = resp['allegiances']
        books = resp['books'] + resp['povBooks']
        if resp['name'] != "":
            print(f"Name: {resp['name']}")
        else:
            print(f"Alias: {resp['aliases'][0]}")

        print("\nALLIES: ")
        for link in allies:
            print(requests.get(link).json()['name'])
            print("\nBOOKS: ")
        for link in books:
            print(requests.get(link).json()['name'])

if __name__ == "__main__":
        main()

