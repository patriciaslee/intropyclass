#Melinda Guillory
#Lab 2, Guessing Game

#Retrieve the initial user Guess as an integer
userGuess = int(input('Guess a number from 1 to 10. (Please enter 0 if you wish to end this simulation.): 0 '))
#Set the Correct Number to 6
correctNum = 6

#Exit while loop if user selects 0 or the correct Number
while userGuess != 0 or userGuess == correctNum:

    #Check the conditions for the correct number
    if userGuess < 1 or userGuess > 10:
        print ("That is not a number from 1 to 1")
    elif  userGuess < correctNum:
        print ("That is too low!")
    elif  userGuess > correctNum:
        print ("That is too high!")
    else:
        userGuess == correctNum
        print ("That is correct!")
        break;
    
    #Retrieve a new guess as an integer
    userGuess = int(input('Guess again!. (Number from 1 to 10, 0 to end.): '))

print('End Simulation')
        
    
