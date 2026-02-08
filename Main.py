#Game functions modules
import guess_number 
import rock_paper_scissors as rps
import Hangman as hangman
# import MathGame as mg
# Gui modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Initialize the main window
root = Tk()
root.title("Ultimate Game Console")
root.geometry("500x400")  # Initial window size
# root.geometry("420x300")  # Initial window size
# root.resizable(False,False)   



#functions to go to each game


def popup(module_name):
    '''Popup Window to reveal the game rules'''
    messagebox.showinfo("game rules",module_name.rules())
def guess_number_window():
    '''The window to play the Guess the number game'''
    root.destroy()
    #define the new window and give it its attributes
    newWindow = Tk()
    newWindow.geometry("500x500")
    newWindow.title("Guess The Number!")
    
    # Guess Number window
    
    #buttons
    rule = Button(newWindow, text="game rules", command= lambda: popup(guess_number))
    rule.pack()

def rps_window():
    '''The window to play Rock Paper Scissors'''

    root.destroy()
    #define the new window and give it its attributes
    newWindow = Tk()
    newWindow.geometry("500x500")
    newWindow.title("Rock Paper Scissors")
    
    # Rock Paper Scissors window
    
    # Images
    img_rock = ImageTk.PhotoImage(Image.open(r"PythonProjects\games\game_Console_Pics\rock.png"))
    img_paper = ImageTk.PhotoImage(Image.open(r"PythonProjects\games\game_Console_Pics\paper.png"))
    img_scissors = ImageTk.PhotoImage(Image.open(r"PythonProjects\games\game_Console_Pics\scissors.png"))
    
    #buttons
    # rule = Button(newWindow, text="game rules", command= lambda: popup(rps))
    label_rock = Label(newWindow,width=50,height=50,image=img_rock)
    # #show Buttons on the screen
    # rule.pack()  
    label_rock.pack()



def hangman_window():
    '''The window to play Hangman'''

    root.destroy()
    #define the new window and give it its attributes
    newWindow = Tk()
    newWindow.geometry("500x500")
    newWindow.title("Hangman")
    
    # Hangman window
    
    #buttons
    rule = Button(newWindow, text="game rules", command= lambda: popup(hangman))
    rule.pack()

#first window

#Label to welcome the player
welcome_Player = Label(root,text="Hello Player! ,Let the games begin!\nPlease Choose a game!",borderwidth=2,border=10, font=("Arial", 18, "bold"))

#Buttons to choose the game
button_guess_number = Button(root ,text="Guess Number",width=40,pady=10,borderwidth=2,border=8,command=guess_number_window)
button_rps = Button(root ,text="Rock Paper Scissors",width=40,pady=10,borderwidth=2,border=8,command=rps_window)
button_Hangman = Button(root ,text="Hangman",width=40,pady=10,borderwidth=2,border=8,command=hangman_window)
button_quit = Button(root,text="Quit",width=20,pady=10,borderwidth=2,border=5,command=root.quit)

#Put The buttons in place
welcome_Player.pack(pady=10)
button_guess_number.pack(pady=10)
button_rps.pack(pady=10)
button_Hangman.pack(pady=10)
button_quit.pack(pady=10)


root.mainloop()