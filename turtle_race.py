import turtle
import random

p_one = turtle.Turtle()
p_one.color("purple")
p_one.shape("turtle")
p_one.penup()
p_one.goto(-200,100)
p_two = p_one.clone()
p_two.color("orange")
p_two.penup()
p_two.goto(-200,-100)

p_one.goto(300,60)
p_one.pendown()
p_one.circle(40)
p_one.penup()
p_one.goto(-200,100)
p_two.goto(300,-140)
p_two.pendown()
p_two.circle(40)
p_two.penup()
p_two.goto(-200,-100)

die = [1,2,3,4,5,6]
for i in range(20):
    if p_one.pos() >= (300,100):
            print("Player One Wins!")
            break
    elif p_two.pos() >= (300,-100):
            print("Player Two Wins!")
            break
    else:
            p_one_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("Result of the die roll is: ")
            print(die_outcome)
            print("Number of steps will be: ")
            print(20*die_outcome)
            p_one.fd(20*die_outcome)
            p_two_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("Result of the die roll is: ")
            print(die_outcome)
            print("Number of steps will be: ")
            print(20*die_outcome)
            p_two.fd(20*die_outcome)