import os
import random

"""Based on Datacamp exercises and the hangman art in this gist: 
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c """


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
        "nestjs",
        "flask",
        "aspnet",
        "meteor",
        "emberjs",
        "nodejs"
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
                print("")
                print("Nice one, keep it up")
                print("")
                found = True

        if not found:
            print("")
            print("You failed")
            attempts -= 1
            print("Remaining attempts: ", attempts)

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
    print("You have 6 attempts")
    game()
