'''example of if else  '''

SECRET: int = 3

print('Im thinking of a number bt 1 and 5. What is it?')
guess: int = int(input('What is you guess? '))

if SECRET == guess:
    print ('Correct')
else:
    print('Game over')  