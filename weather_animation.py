import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Simple Weather Animation")
screen.setup(600, 400)

# Create turtles
sun = turtle.Turtle()
cloud = turtle.Turtle()
rain = turtle.Turtle()

def setup_turtles():
    # Sun turtle
    sun.speed(0)
    sun.hideturtle()
    sun.penup()
    
    # Cloud turtle  
    cloud.speed(0)
    cloud.hideturtle()
    cloud.penup()
    
    # Rain turtle
    rain.speed(0)
    rain.hideturtle()
    rain.penup()
    rain.color("blue")

def draw_sun():
    sun.clear()
    sun.goto(200, 150)
    sun.pendown()
    sun.color("yellow")
    sun.begin_fill()
    sun.circle(40)
    sun.end_fill()
    
    # Sun rays
    for i in range(12):
        sun.penup()
        sun.goto(200, 190)
        sun.pendown()
        sun.forward(60)
        sun.backward(60)
        sun.left(30)

def draw_cloud(x, y):
    cloud.goto(x, y)
    cloud.color("white")
    cloud.pendown()
    cloud.begin_fill()
    
    for i in range(4):
        cloud.circle(20)
        cloud.forward(40)
    
    cloud.end_fill()
    cloud.penup()

def draw_rain():
    rain.clear()
    
    for i in range(20):
        x = random.randint(-250, 250)
        y = random.randint(-150, 100)
        
        rain.goto(x, y)
        rain.pendown()
        rain.forward(30)
        rain.penup()

def sunny_weather():
    screen.bgcolor("lightblue")
    sun.showturtle()
    cloud.hideturtle()
    rain.hideturtle()
    
    draw_sun()
    
    # Draw some clouds
    draw_cloud(-100, 120)
    draw_cloud(0, 100)
    draw_cloud(150, 80)

def cloudy_weather():
    screen.bgcolor("gray")
    sun.hideturtle()
    cloud.showturtle()
    rain.hideturtle()
    
    # Draw many clouds
    draw_cloud(-150, 120)
    draw_cloud(-50, 100)
    draw_cloud(50, 130)
    draw_cloud(150, 110)
    draw_cloud(-100, 80)
    draw_cloud(100, 90)

def rainy_weather():
    screen.bgcolor("darkgray")
    sun.hideturtle()
    cloud.showturtle()
    rain.showturtle()
    
    # Draw clouds
    draw_cloud(-150, 120)
    draw_cloud(0, 130)
    draw_cloud(150, 110)
    
    # Draw rain
    draw_rain()

def change_weather():
    # Choose random weather
    weather = random.choice(["sunny", "cloudy", "rainy"])
    
    if weather == "sunny":
        sunny_weather()
        print("Weather: Sunny")
    elif weather == "cloudy":
        cloudy_weather()
        print("Weather: Cloudy")
    else:
        rainy_weather()
        print("Weather: Rainy")
    
    # Change weather every 3 seconds
    screen.ontimer(change_weather, 3000)

# Start the animation
setup_turtles()
change_weather()

# Click to exit
screen.exitonclick()