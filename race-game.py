from turtle import *
import math
import pygame

# Made by lvxq37-2
# I intentionally kept functions beside their calls so it is clear where the code is used

# Setting up: Background
t = Turtle()
title("Race mini-game")
t.screen.setup(800, 600)
t.screen.bgpic('race-game-files/grassy background.png')

# Setting up: Background Music
# Please run 'python3 -m pip install -U pygame --user' in the terminal if you are experiencing issues with Pygame, or consult the Pygame wiki: https://www.pygame.org/wiki/GettingStarted
pygame.mixer.init()
pygame.mixer.music.load("race-game-files/Wallpaper.mp3") 
pygame.mixer.music.play(-1,0.0)                             # Music is looped until the game is closed

# Setting up: Finish line
finish_l = 220
t.speed(10000)
t.hideturtle()
t.color('red')
t.pensize(5)
t.penup()
t.goto(finish_l, 180)
t.right(90)
t.pendown()
t.forward(360)
t.penup()

# Music toggle
def toggle(x, y):
    PAUSE.toggle()

class Pause(object):

    def __init__(self):
        self.paused = pygame.mixer.music.get_busy()

    def toggle(self):
        if self.paused:
            pygame.mixer.music.pause()
        if not self.paused:
            pygame.mixer.music.unpause()
        self.paused = not self.paused

PAUSE = Pause()                 # PAUSE now has attributes of class Pause

# Button for toggle button
b = Turtle()                    # b stands for button
b.hideturtle()
b.speed(10000)
b.penup()
b_x = finish_l + 60
b_y = 230
b.goto(b_x, b_y)
b.pencolor('black')
b.fillcolor('red')
b.shape('circle')

# Text for button
CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Ariel', FONT_SIZE, 'bold')
b.write("Music", align = "center", font=FONT)
b.sety(b_y + CURSOR_SIZE + FONT_SIZE)
b.onclick(toggle)
b.showturtle()

# Setting up: Players at Start Line
start_l = -260
p1 = Turtle()
p1.shape('turtle')
p1.fillcolor('yellow')
p1.penup()
p1.goto(start_l, 100)

p2 = Turtle()
p2.shape('turtle')
p2.fillcolor('blue')
p2.penup()
p2.goto(start_l, -100)

# Dice
dice_val = ['1', '2', '3', '4', '5', '6']

# In a standard game, players need to move 480 pixels to win.
# A score of 1 will move the player forward by 22 pixels 
# This amounts to a maximum of 20 moves (or minimum of 4) in order for a player to win

# This calculates the maximum number of turns per player. This may change from 20 if the starting or finish lines are changed
max_turns = math.ceil((finish_l - start_l)/22)

def welcome():
    print("\nPlease have 1 die ready before you start the game.\nRemember: entering an invalid dice roll will result in a penalty - You'll miss your turn!\n")
    p1_name = input("Player 1, please enter your name or press enter to skip: ")
    p1_name = "Player 2" if p1_name is "" else p1_name
    p2_name = input("Player 2, please enter your name or press enter to skip: ")
    p2_name = "Player 2" if p2_name is "" else p2_name
    print("Welcome " + p1_name + " and " + p2_name + "!\n")
    return str(p1_name), str(p2_name)

def reset():
    p1.right(180)
    p1.goto(start_l, 100)
    p1.left(180)
    
    p2.right(180)
    p2.goto(start_l, -100)
    p2.left(180)

def check(position):
    if p1.pos() >= (finish_l, 100):
        return True
    elif p2.pos() >= (finish_l, -100):
        return True

def game(p1_name, p2_name):
    for i in range(max_turns): # Maximum limit is standard 20 moves (valid or invalid) per player
        p1_roll = input(p1_name + ", please enter the number you rolled on your die: ")
        if not p1_roll:
            print("You didn't enter anything, skip!")
        elif p1_roll in dice_val:
            print(p1_name, "moves forward", p1_roll, "steps")
            p1.forward(22*int(p1_roll))
            if check(position) == True:
                print("\n" + p1_name + " wins! Well done")
                break
        else:
            print("Skip!")

        p2_roll = input(p2_name + ", please enter the number you rolled on your die: ")
        if not p2_roll:
            print("You didn't enter anything, skip!")
        elif p2_roll in dice_val:
            print(p2_name, "moves forward", p2_roll, "steps")
            p2.forward(22*int(p2_roll))
            if check(position) == True:
                print("\n" + p2_name + " wins! Well done")
                break
        else:
            print("Skip!")


def main(p1_name, p2_name):
    game(p1_name, p2_name)
    rematch = input("Would you like a rematch? y/n: ")
    if rematch.upper() == "Y":
        print("\n")
        reset()
        main(p1_name, p2_name)
    else:
        print("Thanks for playing, goodbye :)")
        bye()

p1_name, p2_name = welcome()
main(p1_name, p2_name)