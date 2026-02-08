from tkinter import *
import guess_number 

#initialize the root app
root = Tk()
root.title("Number Guessing")

#Put on the rules on the screen 
game_rule = guess_number.rules()
rules = Label(root, text = game_rule,font=("Arial",18,"bold"))
rules.pack()


root.mainloop()