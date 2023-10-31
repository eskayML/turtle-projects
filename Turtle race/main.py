from turtle import Turtle, Screen
import random, time
from tkinter import *
from tkinter import messagebox
final_text=''
screen = Screen()
scr_width=800
scr_height=600
screen.setup(width=scr_width, height=scr_height)
turtles = []
color = ['red', 'blue', 'green', 'yellow', 'orange', 'black', 'purple']
interval = 30
y_end = -70
color_text = ', '.join([col.capitalize() for col in color])

correct_color = False
while not correct_color:
    bet = screen.textinput('Welcome to Turtle Races ! ', "Which Turtle would you like to bet on?: "+color_text)
    if bet.lower() not in color:
        bet = screen.textinput('Welcome to Turtle Races ! ',
                               "Incorrect choice ! Which Turtle would you like to bet on?: "+color_text)
    else:
        correct_color=True
        break
for i in range(len(color)):
    turt = Turtle(shape='turtle')
    turt.color(color[i])
    turt.penup()
    y_pos=y_end+interval*i
    turt.setpos(-400, y_pos)
    turtles.append(turt)

if correct_color:
    race_on = True
else:
    race_on=False
#print(race_on)
for i in reversed(range(4)):
    col=turt.color()[0]
    turt.write(str(i+1), font=('Arial, 48'))
    time.sleep(1)
    turt.color('white')
    turt.write(str(i + 1), font=('Arial, 48'))
    turt.color(col)
while race_on:
    for turt in turtles:
        steps = random.randint(0, 10)
        turt.forward(steps)
        if turt.xcor() > (scr_width/2)-10: #turtle size is 20 so 10 is half that (center of mass)
            race_on = False
            turt_winner = turt.color()
            result_text=f'The winner is the {turt.color()[0]} turtle'

final_text+=f'\n\nYou bet on the {bet} turtle'
final_text+=f'\n\nThe winner was the {turt_winner[0].capitalize()} turtle'
if turt_winner[0] == bet:
    title_text='You won!'
    final_text+='\n\nYou won the bet !'
else:
    title_text='You lost!'
    final_text+='\n\nYou lost the bet :('


#from tkinter import * 
from tkinter import messagebox
  
# root = Tk()
#messagebox.showinfo('Final Results of the Race', result_text) # Results
messagebox.showinfo(result_text, final_text) # The alert.
  
#root.mainloop() 