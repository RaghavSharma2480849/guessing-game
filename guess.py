import random
number = random.randint(1,10)
print('number guessing game')
turns = 0
while(turns<5):
    guess = int( input('enter your guess between 1-10 '))
    if(guess==number):
        print('you won')
        break
    elif(guess>number): 
        print('the guess is too high enter a number which is less than ', guess)
    else:
        print('the guess is too low enter a number which is grater than ', guess)
    turns = turns + 1
if(turns == 5): 
    print('you lost')