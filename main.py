from random import randint

words=['Laptop', 'Bee', 'Phone']

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
def scenario_one():
    print("That letter is not part of the word.")
    print('  _____')
    print('  |   |')
    print('  O   |')
    print('      |')
    print('      |')
    print(' _____|___')

def scenario_two():
    print("That letter is not part of the word.")
    print('  _____')
    print('  |   |')
    print('  O   |')
    print('  |   |')
    print('      |')
    print(' _____|___')
    
def scenario_three():
    print("That letter is not part of the word.")
    print('  _____')
    print('  |   |')
    print('  O   |')
    print('  |   |')
    print(' /    |')
    print(' _____|___')

def scenario_four():
    print("That letter is not part of the word.")
    print('  _____')
    print('  |   |')
    print('  O   |')
    print('  |   |')
    print(' / \  |')
    print(' _____|___')

def scenario_five():
    print("That letter is not part of the word.")
    print('  _____')
    print('  |   |')
    print('  O   |')
    print(' /|   |')
    print(' / \  |')
    print(' _____|___')

def scenario_six():
    print("That letter is not part of the word.")
    print('  _____')
    print('  |   |')
    print('  O   |')
    print(' /|\  |')
    print(' / \  |')
    print(' _____|___')
    print('You lost;( better luck next time smelly')

while True:
    for x in range(size_of_word):
        underscores+='_ '
    print(underscores)

    user_guess=input('Please enter a letter: ')

    underscores=''
    for x in range(size_of_word):
        if user_guess==random_word[x]:
            underscores+=str(user_guess)
            count+=1
        else:
            continue

    if(count == 0):
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
        print(underscores)
        count=0




