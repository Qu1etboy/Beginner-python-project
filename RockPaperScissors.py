'''
Python program to play Rock Paper Scissor game with bot
Created by Weerawong Vonggatunyu (Qu1etboy)
Date: 4/9/2022
'''

import random

outcome = ['rock', 'paper', 'scissors']

# introduction
print('Welcome to rock paper scisscors game!')
play = input('Press anything to start (type exit to exit): ')

# game progression
while (play.lower() != 'exit') :
    botInput = random.choice(outcome)
    print('-'*50)
    while (1):
        userInput = input('What do you want to choose ? [rock, paper, scissors]: ').lower()
        if userInput in outcome:
            break 
        else :
            print('Invalid input please try again.')
    
    # result : 0 = draw, 1 = user, 2 = bot
    if userInput == botInput:
        result = 0
    elif userInput[0] == 'r' and botInput[0] == 'p':
        result = 2
    elif userInput[0] == 'r' and botInput[0] == 's':
        result = 1
    elif userInput[0] == 's' and botInput[0] == 'p':
        result = 1
    elif userInput[0] == 's' and botInput[0] == 'r':
        result = 2
    elif userInput[0] == 'p' and botInput[0] == 'r':
        result = 1
    elif userInput[0] == 'p' and botInput[0] == 's':
        result = 2
    
    result = ['Draw', 'Win', 'Lose'][result] 
    print(f'{result}, Opponent choose {botInput}')

    play = input('Play again? [type anything to play again (type exit to exit)]: ')