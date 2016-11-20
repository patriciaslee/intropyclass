# Lab 2

correctNum=6
no=0

guess = input('Guess a number from 1 to 10. (Please enter 0 if you wish to end this simulation.):')
guess=int(guess)

while (1):
    if guess==no:
        break
    elif (guess<0) | (guess>10):
        print ("That is not a number from 1 to 10!")
    elif guess <correctNum:
        print ("That is too low!")
    elif guess >correctNum:
        print ("That is too high!")
    else:
        print ("That is correct!")
        break
    
    guess = input('Guess again! (Number from 1 to 10, 0 to end.):')   
    guess=int(guess)

print ("End Simulation")
