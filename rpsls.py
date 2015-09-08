"""Rice University Interactive Programming
Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of 
Rock-paper-scissors that allows five choices. 
Each choice wins against two other choices, 
loses against two other choices and ties against itself.
Uses modular arithmetic to determine a winner.
"""
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import simpleguitk as simplegui
import random

player_to_print = " "
computer_to_print = " "
winner = " "

def name_to_number(name):
    if name == "rock" or name == "Rock":
        return 0
    elif name == "Spock" or name == "spock":
        return 1
    elif name == "paper" or name == "Paper":
        return 2
    elif name == "lizard" or name == "Lizard":
        return 3
    elif name == "scissors" or name == "Scissors":
        return 4
    else:
        return "Not a valid option"

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Not a valid option"
    
def rpsls(player_choice):
    global player_to_print, computer_to_print, winner
      
    # player choice
    player_to_print = str("Player chooses: " + player_choice)
    player_number = name_to_number(player_choice)
    
    #computer choice
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    computer_to_print = str("Computer chooses: " + comp_choice)
    
    #winner
    winner = (comp_number - player_number) % 5
    if ((player_number - comp_number)%5)>= 3:
        winner = "Computer wins!"
    elif ((player_number - comp_number)%5) == 0:
        winner = "Player and computer tie!"
    else:
        winner = "Player wins!"
        
def restart():
    global player_to_print, computer_to_print, winner
    player_to_print = " "
    computer_to_print = " "
    winner = " "
    
#interactive rpsls

def get_guess(guess):
    #if not an accepted input
    global winner
    if not (guess == "rock" or guess == "Rock" or guess == "Spock" or guess == "spock" 
            or guess == "paper" or guess == "Paper" or guess == "lizard" or
            guess == "Lizard" or guess == "scissors" or guess == "Scissors"):
        winner = 'Error: Bad input, not an included choice'
    else:
        rpsls(guess)
        
def draw(canvas):
    #draw output in frame
    canvas.draw_text(player_to_print, [20, 50], 20, "Green")
    canvas.draw_text(computer_to_print, [20, 85], 20, "Green")
    canvas.draw_text(winner, [20, 125], 20, "Green")
    
#create frame
frame = simplegui.create_frame("Rock-Paper-Scissors-Lizard-Spock", 400, 200)
frame.add_input("Player Choice", get_guess, 200)
frame.set_canvas_background("Pink")
frame.set_draw_handler(draw)
frame.add_button("Clear board", restart, 100)

frame.start()