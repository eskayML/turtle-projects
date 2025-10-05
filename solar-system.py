import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System")
screen.setup(1000, 800)
screen.tracer(0)

class Sun:
    def __init__(self, radius):
        self.radius = radius
        self.x = 0
        self.y = 0
        self.sun_turtle = turtle.Turtle()
        self.sun_turtle.color("yellow")
        self.sun_turtle.penup()
        self.sun_turtle.goto(self.x, self.y - self.radius)
        self.sun_turtle.pendown()
        self.sun_turtle.begin_fill()
        self.sun_turtle.circle(self.radius)
        self.sun_turtle.end_fill()
        self.sun_turtle.penup()

class Planet:
    def __init__(self, name, radius, orbit_radius, speed, color):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.speed = speed
        self.angle = 0
        self.color = color
        self.planet_turtle = turtle.Turtle()
        self.planet_turtle.shape("circle")
        self.planet_turtle.color(self.color)
        self.planet_turtle.penup()
        self.planet_turtle.goto(self.orbit_radius, 0)
        self.planet_turtle.pendown()

    def move(self):
        self.angle += self.speed
        if self.angle >= 360:
            self.angle = 0
        new_x = self.orbit_radius * math.cos(math.radians(self.angle))
        new_y = self.orbit_radius * math.sin(math.radians(self.angle))
        self.planet_turtle.goto(new_x, new_y)

def create_solar_system():
    sun = Sun(30)

    mercury = Planet("Mercury", 5, 60, 1.6, "gray")
    venus = Planet("Venus", 10, 90, 1.2, "yellowgreen")
    earth = Planet("Earth", 12, 120, 1, "blue")
    mars = Planet("Mars", 8, 150, 0.8, "red")
    jupiter = Planet("Jupiter", 30, 200, 0.4, "orange")
    saturn = Planet("Saturn", 25, 250, 0.3, "goldenrod")
    uranus = Planet("Uranus", 20, 300, 0.2, "lightblue")
    neptune = Planet("Neptune", 18, 350, 0.1, "darkblue")

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    def animate():
        for planet in planets:
            planet.move()
        screen.update()
        screen.ontimer(animate, 50)

    animate()
    screen.exitonclick()

create_solar_system()

