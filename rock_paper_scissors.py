import random as rand
#Possible choices
RPS = ['Rock','Paper','Scissors']

def rules():
    '''
    Prints the rules of the game
    '''
    game_rules = '''Welcome to Rock, Paper, Scissors!

In this classic game, you'll be facing off against the computer in a battle of wits and quick decision-making. The rules are straightforward:

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock

Here's how it works:
1. You and the computer will both choose one of the three options: Rock, Paper, or Scissors.
2. The winner of each round is determined by the interactions between the choices: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
3. The game is played in a series of rounds, and the player with the most victories at the end is declared the overall winner.

To make your choice, simply type 'rock', 'paper', or 'scissors' when prompted. The computer will randomly select its choice, and the winner of each round will be announced.

Are you ready? Let the Rock, Paper, Scissors showdown begin!
'''
    return game_rules
def is_valid(choice):
    '''
    checks if the choice is rock ,paper or scissors
    '''
    return  choice.capitalize() in RPS
def play():
    while True:
        #Print the rules to the user
        rules()
        
        #randomize the choice of the computer
        p1 = rand.choice(RPS)
        while True:
            choice = input('Choose rock, paper or scissors :').capitalize()
            match(is_valid(choice)):
                case True:
                    print (f"You chose : {choice} and The computer chose : {p1}")
                    if choice == 'Rock':
                        if p1 == 'Rock':
                            print("IT'S A DRAW!")
                        elif p1 == 'Paper':
                            print("The computer Won!")
                        else:
                            print("YOU WON!")  
                    elif choice == 'Paper':
                        if p1 == 'Rock':
                            print("YOU WON!")  
                        elif p1 == 'Paper':
                            print("IT'S A DRAW!")
                        else:
                            print("The computer Won!")
                    
                    elif choice == 'Scissors':
                        if p1 == 'Rock':
                            print("The computer Won!")
                        elif p1 == 'Paper':
                            print("YOU WON!")  
                        else:
                            print ("IT'S A DRAW!")
 
                    break          
                case False:
                    print("Invalid choice. Please choose rock, paper, or scissors.")
                    break
        play_again = input("Do you want to play again? (yes/no)").strip().lower()        
        if play_again != 'yes':
            break               



