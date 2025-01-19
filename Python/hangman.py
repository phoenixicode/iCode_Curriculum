#HangMan Game using Strings
import random

def display_word(word, guessed_letters):
  return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def hangman():
    word = random.choice([
                             "tesla",       # 5 characters
                             "ford",        # 4 characters
                             "nissan",      # 6 characters
                             "honda",       # 5 characters
                             "fiat",        # 4 characters
                             "kia",         # 3 characters
                             "jeep",        # 4 characters
                             "mazda",       # 5 characters
                             "chery",       # 5 characters
                             "rover"        # 5 characters
 ])
    print("welcome to hangman")
    usr_input = ''
    tries = 10
    fails = 0
    sucess = 0
    guessed = []
    while tries > 0:
      usr_input = input("enter a word")

      if usr_input in word:
          print(f'correct {usr_input} is in the word')
          tries = tries + 1
          sucess = sucess + 1
          print(f'you have {tries} tries left')
          #to show the word in underrscores
          guessed.append(usr_input)
          print(display_word(word, guessed))
          if sucess == len(word):
            print("you won")
            break

      else:
        print(f'wrong {usr_input} is not in the word')
        tries = tries - 1
        print(f'you have {tries} tries left')
        fails = fails + 1



hangman()
