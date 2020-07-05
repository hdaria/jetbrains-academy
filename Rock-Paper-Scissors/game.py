# Write your code here
import random


def user_lose(user, comp):
    lose_options = []
    position = 0
    lose_count = len(options) // 2
    for i, val in enumerate(options):
        if val == user:
            position = i
            break
    if position < lose_count:
        lose_options.extend(options[:position])
        lose_options.extend(options[position - lose_count:])
    else:
        lose_options.extend(options[position - lose_count:position])

    if comp not in lose_options:
        return True
    return False


option = ["rock", "paper", "scissors"]
answer = dict(Lose='Sorry, but computer chose {}', Draw='There is a draw ({})',
              Win='Well done. Computer chose {} and failed')

name = input("Enter your name: ")
print(f"Hello, {name}")

rating = 0

file = open('rating.txt', 'r')
for line in file:
    string = line.split()
    if string[0] == name:
        rating = int(string[1])
        break
file.close()

options = input()
if len(options) == 0:
    options = option
else:
    options = options.split(',')
print("Okay, let's start")

while True:
    user_choice = input()
    if user_choice == "!rating":
        print(f"Your rating: {rating}")
        continue
    if user_choice == "!exit":
        print("Bye!")
        break
    if user_choice not in options:
        print("Invalid input")
        continue
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = 'Draw'
        rating += 50
    elif user_lose(user_choice, computer_choice):
        result = 'Lose'
    else:
        result = 'Win'
        rating += 100
    print(answer[result].format(computer_choice))
