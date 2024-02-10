import turtle
import math


# Define the CelestialBody class
class CelestialBody:
    def __init__(self, name, color, size, orbit_radius, speed):
        self.name = name
        self.color = color
        self.size = size
        self.orbit_radius = orbit_radius
        self.speed = speed
        self.angle = 0
        self.body = turtle.Turtle()
        self.body.penup()
        self.body.shape("circle")
        self.body.color(color)
        self.body.shapesize(size)
        self.body.speed(0)  # Set the drawing speed to the maximum

    def orbit(self):
        x = self.orbit_radius * math.cos(math.radians(self.angle))
        y = self.orbit_radius * math.sin(math.radians(self.angle))
        self.body.goto(x, y)
        self.angle += self.speed


# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("The Miles System")


# Function to draw orbit paths
def draw_orbit(turtle, radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()


# Create a turtle for drawing orbit paths
orbit_drawer = turtle.Turtle()
orbit_drawer.speed(0)
orbit_drawer.color("grey")
# orbit_drawer.penup()  # Add this line to lift the pen
orbit_drawer.hideturtle()

# Draw orbit paths for each planet
draw_orbit(orbit_drawer, 50)
draw_orbit(orbit_drawer, 80)
draw_orbit(orbit_drawer, 110)
draw_orbit(orbit_drawer, 150)

# Create the sun
sun = CelestialBody("Sun", "yellow", 2, 0, 0)

# Create planets: name, color, size, orbit_radius, speed
mercury = CelestialBody("Mercury", "grey", 0.7, 50, 2)
venus = CelestialBody("Venus", "orange", 1, 80, 1.5)
earth = CelestialBody("Earth", "blue", 1.2, 110, 1)
mars = CelestialBody("Mars", "red", 1, 150, 0.8)

# Main animation loop
while True:
    mercury.orbit()
    venus.orbit()
    earth.orbit()
    mars.orbit()
