#!/usr/bin/env python3
farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

for x in range(len(farms)):
    for value in farms[x]:
        if farms[x][value] == "NE Farm":
            for agriculture in farms[x]["agriculture"]:
                print(agriculture)

print()
print()
user_farm1 = input("Choose a farm. (NE Farm, W Farm, E Farm, or SE Farm) ")
for x in range(len(farms)):
    for value in farms[x]:
        if farms[x][value] == user_farm1:
            for agriculture in farms[x]["agriculture"]:
                print(agriculture)

print()
print()
user_farm2 = input("Choose a farm. (NE Farm, W Farm, E Farm, or SE Farm) ")
for x in range(len(farms)):
    for value in farms[x]:
        if farms[x][value] == user_farm2:
            for agriculture in farms[x]["agriculture"]:
                if agriculture in animals:
                    print(agriculture)
