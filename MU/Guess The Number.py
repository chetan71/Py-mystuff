#Guess the number Programe
import random

print ('guess the number!!!')
print ('I am thinking of a number between 1 and 20')
print ('Take a guess')
Number=random.randint(1, 20)
Guess= 0
Guesses=0
while Guess!=Number:
    Guess= int(input('-'))

    Guesses=Guesses+1
    if Guess > Number:

        print('Your guess is to high')
    elif Guess<Number:
        print('Your guess is to low')
    else:
        print('Good job! You guessed my number in '+str(Guesses)+' guesses.')
        break
