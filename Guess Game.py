print('Welcome to this Game')
print('In this game you will have to guess a number between 1 and 100 and if the number matches with your guess you get an increase in the score')
import random
a=random.randint(1,100)
score=0
while True:
    b=int(input('Please enter your guess'))

    if a==b:
        score=score+1
        print('Congratulations, you guessed the number and your score is',score)
        break
    elif b<a:
        print(a)
        print(b) 
        print('Your guess is too low, try again')
    else:
        print(a)
        print(b)
        print('Your guess is too high, try again')
    
c=d