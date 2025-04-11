import turtle
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Enhanced Fireworks 🎆")
screen.setup(width=800, height=600)
screen.tracer(0)  # turn off auto-refresh for smooth animation

# Color mode
turtle.colormode(255)

# Create a turtle for fireworks
firework = turtle.Turtle()
firework.hideturtle()
firework.penup()
firework.speed(0)

# Create multiple spark particles
def explode_firework(x, y):
    sparks = []

    num_sparks = random.randint(15, 30)
    colors = [
        (255, 255, 102), (255, 102, 102), (102, 255, 178),
        (255, 153, 255), (102, 178, 255), (255, 255, 255)
    ]
    color = random.choice(colors)

    for _ in range(num_sparks):
        spark = turtle.Turtle()
        spark.shape("circle")
        spark.color(color)
        spark.shapesize(0.3)
        spark.penup()
        spark.speed(0)
        spark.goto(x, y)

        angle = random.uniform(0, 360)
        distance = random.uniform(20, 100)
        sparks.append((spark, angle, distance))

    # Animate the sparks
    for step in range(20):
        for spark, angle, distance in sparks:
            spark.setheading(angle)
            spark.forward(distance / 20)
            spark.shapesize(max(0.3 - step * 0.01, 0.01))  # shrink spark
        screen.update()
        time.sleep(0.03)

    # Remove all sparks
    for spark, _, _ in sparks:
        spark.hideturtle()

# Click event
screen.onclick(explode_firework)

# Keep the window open
screen.mainloop()
