from tkinter import *
import random


# --- Function to start new game ---
def new_game():
    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

# --- function to change turn ---
def next_turn(row, column):
     global player

     if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
                
            elif check_winner() == "Draw":
                label.config(text="It's a draw!")
                
        else:
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
                
            elif check_winner() is True:
                label.config(text=(players[1]+ "wins!"))
                
            elif check_winner() == "Draw":
                label.config(text="It's a draw!")
                
# --- Function to check for winner ---
def check_winner():
    # check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="": 
            buttons[row][0].config(bg="light blue")
            buttons[row][1].config(bg="light blue")
            buttons[row][2].config(bg="light blue")
            return True
        
    # check columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="light blue")
            buttons[1][column].config(bg="light blue")
            buttons[2][column].config(bg="light blue")
            return True
        
    # check diagnoals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="light blue")
        buttons[1][1].config(bg="light blue")
        buttons[2][2].config(bg="light blue")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="light blue")
        buttons[1][1].config(bg="light blue")
        buttons[2][0].config(bg="light blue")
        return True
    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#F75E5E")
        return "Draw"
    else:
        return False

# --- Function to check for empty spaces ---
def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

# --- Main game logic ---

#create the window
window = Tk()
window.title("Tic-Tac-Toe") #title of the window

#create two players of X and O
players = ["X","O"]
player = random.choice(players) #randomly choose X or O to start

#create the game board (buttons)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text = player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game) #start new game
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40),width=5, height=2, command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()