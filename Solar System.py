import turtle

# Setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Solar System Animation")

# Creating a Turtle object for drawing the sun and planets
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)

# Creating a list of planets with their properties (color, distance from the sun, size, and speed)
planets = [
    {"color": "gray", "distance": 50, "size": 0.5, "speed": 1},
    {"color": "orange", "distance": 80, "size": 0.8, "speed": 0.5},
    {"color": "red", "distance": 120, "size": 0.7, "speed": 0.3},
    {"color": "blue", "distance": 160, "size": 0.6, "speed": 0.2},
    {"color": "green", "distance": 200, "size": 0.9, "speed": 0.1}
]

# Creating a Turtle object for each planet and animate their orbits
planet_turtles = []
for planet in planets:
    planet_turtle = turtle.Turtle()
    planet_turtle.shape("circle")
    planet_turtle.color(planet["color"])
    planet_turtle.shapesize(planet["size"])
    planet_turtle.penup()
    planet_turtle.goto(planet["distance"], 0)
    planet_turtle.pendown()
    planet_turtles.append(planet_turtle)

# Function to animate the planets' orbits
def animate_orbits():
    for i, planet in enumerate(planet_turtles):
        planet.speed(0)
        angle = 360 * planets[i]["speed"]
        planet.circle(planets[i]["distance"], angle)

# Animating the orbits
while True:
    animate_orbits()
    wn.update()

# Closing the program when the user clicks on the screen
wn.exitonclick()


