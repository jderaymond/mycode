#!/usr/bin/env python3

from random import randint
#Create a list of possible disney princesses
disney_princess = ["Moana", "Ariel", "Jasmine", "Cinderella", "Mulan", "Pochahontas", "Snow White", "Rapunzel"]

print('''
        --------------------------------------
        |                                    |
        |                                    |
        |                                    |
        |   What Disney Princess are you?    |
        |                                    |
        |                                    |
        |                                    |
        --------------------------------------
       ''')

month = input("What month were you born? (January, February, March, etc.) ")

while True: 
    if month.lower() == 'january' or month.lower() == 'february':
        disney_princess.remove("Jasmine")
        break

    elif month.lower() == 'march' or month.lower() == 'april':
        disney_princess.remove("Cinderella")
        break
    elif month.lower() == 'may' or month.lower() == 'june':
        disney_princess.remove("Mulan")
        break
    elif month.lower() == 'july' or month.lower() == 'august':
        disney_princess.remove("Pochahontas")
        break
    elif month.lower() == 'september' or month.lower() == 'october':
        disney_princess.remove("Snow White")
        break
    elif month.lower() == 'november' or month.lower() == 'december':
        disney_princess.remove("Rapunzel")
        break
    else:
        print(f"Try again {month} is not a valid month.")
        month = input("What month were you born? (January, February, March, etc.)")

day = int(input("What day of the month were you born on? "))
#after dealing with the months there should be 7 princesses left
while True:
    if day >= 1 and day <= 9:
        remainder = day % 2
        del disney_princess[remainder]
        break
    elif day > 9 and day <= 18:
        remainder = day % 3
        del disney_princess[remainder]
        break
    elif day > 18 and day <= 28:
        remainder = day % 4
        del disney_princess[remainder]
        break
    elif day > 28 and day <= 31:
        del disney_princess[-1]
        break
    else:
        print(f"Try again {day} is not a valid day.")
        day = input("What day of the month were you born on?")
    
military_branch = input("What branch of the military are/were you in? (Air Force, Army, Coast Guard, Marine Corps, Navy, None) ")
while True:
#after dealing with the days there should be 6  princesses left
    print()
    if military_branch.lower() == 'air force':
        if "Jasmine" in disney_princess:
            print("Your disney princess is Jasmine.")
            break
        else:
            princess = disney_princess.pop(-1)
            print(f"Your disney princess is {princess}.")
            break
        break
    if military_branch.lower() == 'army':
        if "Mulan" in disney_princess:
            print("Your disney princess is Mulan.")
            break
        else:
            princess = disney_princess.pop(-2)
            print(f"Your disney princess is {princess}.")
            break
        break
    if military_branch.lower() == 'coast guard':
        if "Moana" in disney_princess:
            print("Your disney princess is Moana.")
            break
        else:
            princess = disney_princess.pop(-3)
            print(f"Your disney princess is {princess}.")
            break
        break
    if military_branch.lower() == 'marine corps':
        if "Cinderella" in disney_princess:
            print("Your disney princess is Cinderella.")
            break
        else:
            princess = disney_princess.pop(-4)
            print(f"Your disney princess is {princess}")
            break
        break
    if military_branch.lower() == 'navy':
        if "Ariel" in disney_princess:
            print("Your disney princess is Ariel.")
            break
        else:
            princess = disney_princess.pop(-5)
            print(f"Your disney princess is {princess}")
            break
        break
    if military_branch.lower() == 'none':
        random_index = randint(0,5)
        princess = disney_princess.pop(random_index)
        print(f"Your disney princess is {princess}.")
        break
    else:
        print(f"Try again {military_branch} is not a valid answer.")
        
