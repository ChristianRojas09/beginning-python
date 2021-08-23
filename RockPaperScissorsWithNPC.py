# This is a rock paper scissors game
import random

print('Rock...')
print('Paper...')
print('Scissors...')

player = input('Choose your weapon:').lower()

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

#the following creates random number generator and assigns it
rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = rock
elif rand_num == 1:
    computer = paper
else:
    computer = scissors
print(f'Computer plays {computer}')

#run through the posibilities
if player == computer:
    print('It is a tie!')
elif player == rock:
    if computer == scissors:
        print('player wins!')
    elif computer == paper:
        print('Computer wins!')
elif player == paper:
    if computer == scissors:
        print('Computer wins!')
    elif computer == rock:
        print('Player wins!')
elif player == scissors:
    if computer == rock:
        print('Computer wins!')
    elif computer == paper:
        print('Player wins!')
else:
    print('pick your weapon!!')