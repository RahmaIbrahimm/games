import guess_number 
import rock_paper_scissors as rps
import Hangman as hangman
import math_game  
import tkinter as tk
# import customtkinter as ctk
# '''
#     A game console made of simple games , the user can choose of a variety of old school games to play and have fun.
#     By Rahma Ibrahim Elshabrawy 

# '''


#==============================================================================================
def is_valid(inpt):
    '''
    Checks whether the input is in range or not
    Returns True if in range of 1 to 4, otherwise False.
    '''
    try:
        inpt = int(inpt)
        return 1<= inpt <=4
    except ValueError:
        print("Please choose a whole number between 1 and 4")
        game_menu()
               
    #the player chooses what game they want to play. 
def game_menu():
    '''
    Game menu displayed and the player chooses which game to be played.
    '''
    while True:
        gameplay = input('''Welcome to the Game menu!
Choose what game you want to play :
    1 - Rock Paper Scissors
    2 - Guess the Number
    3 - Hangman
    4 - Math Quiz
    Choose a number (1 - 4): ''').strip()
        
        if is_valid(gameplay):
            return int(gameplay)
        else:
            print("\nInvalid input. Please enter a number between 1 and 4.\n")
    
def game():
    'main function to start playing the game'
    
    while True:
        #Print the game menu and let the user choose the game 
        gameplay = game_menu()
        #let the user play the game chosen.
        match(gameplay):
            case 1:
                rps.play()
            case 2:
                guess_number.play()
            case 3:
                hangman.play()
            case 4:
                math_game.play()
            case _:
                print("FAILED!!!")

        x = input("Type back to go back to the main menu or any letter to exit : ").strip().lower()
        if x == 'back':
            continue
        else:
            break
        
game()         
#file for high scores , the user enters their username. 

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
game = ctk.CTk()
game.title("Game console")
game.geometry("500x500")

game.mainloop()


