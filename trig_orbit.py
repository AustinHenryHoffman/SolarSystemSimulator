import turtle
import math
import time

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

        # Draw the right triangle for visualization
        self.draw_triangle()

    def draw_triangle(self):
        # Draw the right triangle to visualize the position calculation
        triangle_drawer = turtle.Turtle()
        triangle_drawer.speed(0)
        triangle_drawer.color("white")
        triangle_drawer.hideturtle()

        # Draw the radius line
        triangle_drawer.penup()
        triangle_drawer.goto(0, 0)
        triangle_drawer.pendown()
        triangle_drawer.goto(self.orbit_radius * math.cos(math.radians(self.angle)),
                              self.orbit_radius * math.sin(math.radians(self.angle)))

        # Draw the horizontal line (x-axis)
        triangle_drawer.penup()
        triangle_drawer.goto(0, 0)
        triangle_drawer.pendown()
        triangle_drawer.goto(self.orbit_radius * math.cos(math.radians(self.angle)), 0)

        # Draw the vertical line (y-axis)
        triangle_drawer.penup()
        triangle_drawer.goto(self.orbit_radius * math.cos(math.radians(self.angle)), 0)
        triangle_drawer.pendown()
        triangle_drawer.goto(self.orbit_radius * math.cos(math.radians(self.angle)),
                              self.orbit_radius * math.sin(math.radians(self.angle)))

        time.sleep(.05)  # Add a delay to slow down the animation
        triangle_drawer.clear()  # Clear the triangle after drawing

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("The Miles System")

# Function to draw the orbit path
def draw_orbit(turtle, radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

# Create a turtle for drawing the orbit path
orbit_drawer = turtle.Turtle()
orbit_drawer.speed(0)
orbit_drawer.color("grey")
orbit_drawer.hideturtle()

# Draw the orbit path for Earth
draw_orbit(orbit_drawer, 110)

# Create the sun
sun = CelestialBody("Sun", "yellow", 2, 0, 0)

# Create Earth: name, color, size, orbit_radius, speed
earth = CelestialBody("Earth", "blue", 1.2, 110, 1)

# Main animation loop
while True:
    earth.orbit()

    # Update the screen
    wn.update()
