import art
import random as r
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def difficulty():
  level = input("would you like to play it the hard or easy way? Type hard or easy ").lower()
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
def compare(chosen_number, guessed_number):
  if chosen_number == guessed_number:
    game_continuation = False
    print(f"Wow, great job! You've guessed my number {chosen_number} correctly")
  elif chosen_number < guessed_number:
    print("The number you've chosen is to high. Guess again")
  elif chosen_number > guessed_number:
    print("The number you've chosen is to low. Guess again")

def game():
  print(art.logo)
  print("Welcome to this numbers game where I, the computer, have chosen a number")
  print("between 1 and 100 and you, the gamer, need to guess it.")
  game_continuation = True
  number = 0
  numbers = []
  for number in range(100):
    number += 1
    numbers.append(number)
  chosen_number = r.choice(numbers)
  turns = difficulty()
  while game_continuation:
    for guess in range(turns):
      guessed_number = int(input("Guess the number: "))
      compare(chosen_number, guessed_number)
      if chosen_number == guessed_number:
        game_continuation = False
        break
    if chosen_number != guessed_number: 
      game_continuation = False
      print(f"Your {turns} guesses are up! My number was {chosen_number}")
  another_game = input("Do you want continue game, type yes or no ? ").lower()
  if another_game == "yes":
      os.system('clear')
      game()
  else:
      print("Thank you for a nice game. See you another day!")
      os.system('clear')

game()




  


