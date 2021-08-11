#!/usr/bin/env python3

import requests
import random

def main():
    difficulty = ""
    while difficulty != 'easy' or difficulty != 'medium':
        difficulty = input("What difficulty of questions do you want? (Easy or Medium): ").lower()
        if difficulty == 'easy' or difficulty == 'medium':
            API = f'https://opentdb.com/api.php?category=21&amount=5&difficulty={difficulty}&type=boolean'
            questions = []
            correct_answers = []
            possible_answers = []
            resp = requests.get(API)
            data = resp.json()
            for question in data['results']:
                questions.append(question['question'])
                correct_answers.append(question['correct_answer'])
                #possible_answers.append(question['incorrect_answers'])
                #possible_answers.append(question['correct_answer'])
            break
        else:
            print(f'{difficulty} is not an option. Please select easy or medium')
    
    count = 0
    correct = 0
    while count < 5:
        print()
        print(f"{questions[count]}")
        guess = input("What is your guess?: ").lower()
        if guess == correct_answers[count].lower():
            print('That is correct!!')
            print()
            correct += 1
        else:
            print(f'Sorry the correct answer was {correct_answers[count]}.')
            print()
        count +=1
    if correct == 5:
        print("CONGRATS!! You got all 5 questions right!")
    else:
        print(f"You got {correct} out of 5 correct answers")

if __name__ == "__main__":
  main()
