'''
Python program to play Hangman game.
created by Weerawong Vonggatunyu (Qu1etboy)
Date : 4/7/2022
  ___
 |   |
 |   o
 |  /|\
 |  / \
 |_
'''

import random 

def drawHangman(guessCount):
    if guessCount == 7:
        print(' ___')
        print('|   |')
        print('|')
        print('|')
        print('|')
        print('|_')
    elif guessCount == 6:
        print(' ___')
        print('|   |')
        print('|   o')
        print('|')
        print('|')
        print('|_')
    elif guessCount == 5:
        print(' ___')
        print('|   |')
        print('|   o')
        print('|   |')
        print('|')
        print('|_')
    elif guessCount == 4:
        print(' ___')
        print('|   |')
        print('|   o')
        print('|  /|')
        print('|')
        print('|_')
    elif guessCount == 3:
        print(' ___')
        print('|   |')
        print('|   o')
        print('|  /|\\')
        print('|')
        print('|_')
    elif guessCount == 2:
        print(' ___')
        print('|   |')
        print('|   o')
        print('|  /|\\')
        print('|  /')
        print('|_')
    elif guessCount == 1:
        print(' ___')
        print('|   |')
        print('|   o')
        print('|  /|\\')
        print('|  / \\')
        print('|_')

def showWord(output):
    print('Current Word: ' + ' '.join(output))

def guessCheck(letter, targetWord, output):
    guessRight = False 
    for i in range(len(targetWord)):
        if letter.lower() == targetWord[i].lower():
            output[i] = letter.lower() 
            guessRight = True 
    
    return guessRight

def hangman():
    # game progression
    guessWord = ['elephant', 'tiger', 'cat']
    targetWord = random.choice(guessWord) # use to generate random word from guessWord
    output = ['_'] * len(targetWord)
    usedLetters = set()
    guessCount = 8
    
    while guessCount > 0:
        print('You have used these word : ', ' '.join(list(usedLetters)))
        drawHangman(guessCount)
        showWord(output)
        userGuess = input('Guess a letter : ')
        if userGuess.isalpha():
            if userGuess not in usedLetters:
                usedLetters.add(userGuess)
                if guessCheck(userGuess, targetWord, output) == False :
                    guessCount -= 1
            else :
                print('You have already used this character.')
        else :
            print('Please enter only a character.')
        print('-' * 20)
        word = ''.join(output)
        if word == targetWord :
            showWord(output)
            break

    if guessCount > 0:
        print(f'Congratuation! YOU WON!. The word was {targetWord}')
    else :
        print(f'You are out of guess the correct word is {targetWord}')

# main

print('Welcome to Hangman game!')
while (1):
    mode = input('Enter [1] to start or [0] to exit : ')
    if mode == '0':
        break 
    hangman()
