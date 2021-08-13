#!/usr/bin/env python3

import requests

def init():
    print("""
            _____________________________________
            |                                   |
            |                                   |
            |                                   |
            |       Welcome to MADLIBZ!!        |
            |                                   |
            |                                   |
            |___________________________________|

""")
    #minlength set to 2 so that the madlib "Hello ______!" will not be populated
    minlength = 2
    maxlength = input("What is the maximum number of blanks you would like to fill in?: ")
    while int(maxlength) < 10:
        maxlength = input("There must be at least 10 blanks. How many would you like?: ")
    API = f"http://madlibz.herokuapp.com/api/random?minlength={minlength}&maxlength={maxlength}"
    resp = requests.get(API)
    data = resp.json()
    title = data['title']
    counter = 0 
    blanks= []
    while counter < len(data['blanks']):
        for blank in data['blanks']:
            blanks.append(blank)
            counter += 1
    identifier = 1
    values = []
    while identifier != 0:
        for value in data['value']:
            values.append(value)
            identifier = value
    values.pop()
    return title, blanks, values

def main():
    play_again = 'yes'
    while play_again == 'yes':
        title, blanks, values = init()
        user_answers = []
        for blank in blanks:
            if blank[0] == 'a' or blank[0] == 'e' or blank[0] == 'i' or blank[0] == 'o' or blank[0] == 'u':
                answer = input(f"Provide an {blank}: ")
                while answer in user_answers:
                    answer = input(f"You already used {answer} as a response. Try a new {blank} for maximum fun! ")
                user_answers.append(answer)
            else:
                answer = input(f"Provide a {blank}: ")
                while answer in user_answers:
                    answer = input(f"You already used {answer} as a response. Try a new {blank} for maximum fun! ")
                user_answers.append(answer)
        count = 0
        index = 1
        while count < len(values):
            for line in user_answers:
                values.insert(index, line)
                index += 2
                count += 3

        textfile = open("madlibz.txt", "w+")
        textfile.write('\n' + title + '\n')
        for word in values:
            textfile.write(word)
        textfile.close

        textfile = open("madlibz.txt", "rt")
        result = textfile.read()
        print(result)
        play_again = input("Do you want to play again? (yes or no) ")

if __name__ == "__main__":
    main()
