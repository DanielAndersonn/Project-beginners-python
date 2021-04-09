import random 

def guess(x):
    random_number = random.randint(1,x) 
    guess = 0 
    while guess != random_number:
      guess = int(input("Guess a number between 1 and {x}:"))
      if 10 < random_number:
          print('Sorry.Guess again. To low')
      elif 10 > random_number:
          print(' Sorry guess again to rigth')
    print( 'Yes yo great the number guess {random_number}')
    
guess(10)

def computer_guess(x):
    low = 1
    high = x  
    feedback = ''
    while  feedback != 'C '  and low != high :
        guess = random.randint(low, high)
        fedback = input('Is {guess}  to  hight (H) to low, (L) or correct  ')
        if  feedback == 'h':
            high = guess -1 
        elif fedback == 'l':
            low = guess + 1
    print(" Yes is great {guess}")

computer_guess(10)



