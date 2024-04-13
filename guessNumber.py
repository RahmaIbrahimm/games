import random as rand

#Explain to the user the game rules
def rules():
    '''
    Prints the rules of the game
    '''
    game_rules ='''Welcome to the Number Guessing Game!
I've randomly selected a number between 0 and 100. Your task is to guess the correct number.
After each guess, I'll give you a hint. If your guess is too low, I'll say 'higher,' and if it's too high, I'll say 'lower.' 
Keep guessing until you find the correct number. Once you do, I'll reveal how many guesses it took you. Good luck!\n'''
    return game_rules
# if the number is more than 100 ask the user to choose another
def is_valid(guess,number):
    '''
    checks if the number is in range from 0 to 100 and the number is an integer
    it it's an integer returns True , else false
    
    for example 
    
    guess = 45
        True
    guess = 101 // out of range
        False
    guess = 4.5 // not a whole number
        False
    guess = r //String
        False
            
    '''
    try:
        guess = int(guess)
        return 0 <= guess <= 100
    except ValueError:
        return False
#if the number choosen is more than the num tell the user it's more
def is_larger(guess,number):
    ''' 
    if the guess is larger the number returns true , else false.
    
    '''
    return guess > number

def play():
    #Print the rules
    print(rules())
    #select a random number and initialize the number of guesses to one guess (even if they got it correct it'll be one)
    number = rand.randint(0,100)
    count = 1
    #let the user have their first guess.
    guess = input("Take your first Guess! :")
    #while loop to let the user guess until they get the right number
    while guess != number:
        match(is_valid(guess,number)):
            #if the guess is in range , start the game
            case True:
                #if the number is guessed correctly break the loop
                if int(guess) == number:
                    break
                elif is_larger(int(guess),number):
                    print("lower")
                    count+=1
                    guess = input("Take another Guess: ")
                    continue
                else:
                    print("higher")
                    count+=1
                    guess = input("Take another Guess: ")
                    continue
            #if false (not valid) inform the user to choose another number
            case False:
                guess= input("Please enter a whole number between 0 and 100: ")
                continue
    #inform the user that they got it right! 
    print(f"Good Job!\nthe number is: {number} and the number of guesses are {count}.")
    #Ask if the player wants to play again.
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes" or play_again == 'y':
        play()
    else:
        print("Thanks for playing!\n")        
