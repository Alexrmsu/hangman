import os
import random

def game():
    game_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    frameworks = [
        "angular",
        "django",
        "spring",
        "rubyonrails",
        "laravel",
        "vuejs",
        "angularjs",
        "react",
        "nextjs",
        "nestjs"
    ]

    word = random.choice(frameworks)
    spaces = ["_"] * len(word)
    attempts = 6

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(game_art[attempts])
        letter = input("Choose a letter: ")

        found = False

        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attempts -= 1

        if "_" not in spaces:
            os.system("cls")
            print("You win")
            input()
            break

        if attempts == 0:
            os.system("cls")
            print("You lose")
            input()
            break


if __name__ == '__main__':
    game()
