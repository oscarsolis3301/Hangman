from random import randint
from tkinter import *
import tkinter

window = Tk(className="Hangman")
window.geometry("200x150+400+300")


def hello():
    print("Hello there!")

button_test = tkinter.Button(window, text="EXIT", command=window.destroy)
button_test.pack(pady=5, side=TOP)


window.mainloop
words=['laptop', 'bee', 'phone']

running = True

random_word=words[randint(0,2)]

size_of_word=len(random_word)

underscores=''

count=0
scenarios = 1


print('Welcome to hangman! <3 by beb & beb')
print('  _____')
print('  |   |')
print('      |')
print('      |')
print('      |')
print(' _____|___')

#scenarios bc beb is smelly <3
scenarios = ['''
That letter is not part of the word.
  _____
  |   |
  O   |
      |
      |
 _____|___''', '''
 That letter is not part of the word.
  _____
  |   |
  O   |
  |   |
      |
 _____|___''', '''
That letter is not part of the word.
  _____
  |   |
  O   |
  |   |
 /    |
 _____|___''', '''
That letter is not part of the word.
  _____
  |   |
  O   |
  |   |
 / \  |
 _____|___''', '''
That letter is not part of the word.
  _____
  |   |
  O   |
 /|   |
 / \  |
 _____|___''', '''
That letter is not part of the word.
  _____
  |   |
  O   |
 /|\  |
 / \  |
 _____|___
You lost;( better luck next time smelly''']

guessed_correctly=0
guessed_letters = size_of_word * ['_']
print(' '.join(guessed_letters))
guesses=[]

scenario_count = 0
GameIsDone = False
def PlayAgain():
    play_again = input("Do you want to play again?")
    return play_again.lower

while True:

    guessed_word=''
    correct_answer = False
    correct_letter_count = 0
    user_guess=input('Please enter a letter: ')

    for x in range(size_of_word):
        if user_guess == random_word[x]:
            guessed_letters[x] = user_guess
            correct_letter_count+=1
            correct_answer = True
    
    if(correct_answer == True):
        print('You found ' + str(correct_letter_count) + " correct letters in the word!")
        print(' '.join(guessed_letters))

    else:
        if(scenario_count==6):
            GameIsDone = True
        else:
            print(scenarios[scenario_count])
            scenario_count+=1
            print(' '.join(guessed_letters))
            continue

    for x in guessed_letters:
        guessed_word+=x

    if(guessed_word == random_word):
        print("YOU HAVE FINISHED THE GAME GG.")
        GameIsDone = True
    else:
        continue 
    if GameIsDone == True:
        if PlayAgain() == "y" or "yes":
            guessed_correctly=0
            random_word=words[randint(0,2)]
            size_of_word = len(random_word)
            guessed_letters = size_of_word * ['_']
            guesses=[]
            scenario_count = 0
            print('\n')
            print('  _____')
            print('  |   |')
            print('      |')
            print('      |')
            print('      |')
            print(' _____|___')
            print(' '.join(guessed_letters))
            GameIsDone = False
        else:
            break






# Unused Code:

   # print(' '.join(guessed_letters))
    #blanks = list('_'*size_of_word)
    #for guess in set(random_word):
        
     #   blanks = [guess if letter == guess else blank for blank, letter in zip(blanks, random_word)]
       # print(''.join(blanks))

  #  if str(user_guess) in str(guesses):
   #     print('Already guessed that')
  #  else:
    #     if user_guess in random_word:
    #        output = [x if x == user_guess else "_" for x in random_word]
    #        guesses.append(user_guess)
     #       print(output)
    
    ''' for position, letter in enumerate(random_word):
      if letter == user_guess:
        guessed_letters[position-1] = letter'''


    ##for x in range(size_of_word):
      #  if user_guess==random_word[x]:
       #     print(random_word[x])
       #     guessed_letters.append(user_guess)
       #     count+=1

''' if(count == 0):
        if scenarios == 1:
            scenario_one()
            scenarios+=1

        elif scenarios == 2:
            scenario_two()
            scenarios+=1

        elif scenarios == 3:
            scenario_three()
            scenarios+=1

        elif scenarios == 4:
            scenario_four()
            scenarios+=1

        elif scenarios == 5:
            scenario_five()
            scenarios+=1

        elif scenarios == 6:
            scenario_six()
            break
        
    else:  
        print("\nYou have found " + str(count) + " letters in the word!")
        print("Your progress so far:")
       # print(underscores)
        count=0
        guessed_correctly+=1
'''



