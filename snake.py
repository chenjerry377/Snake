import random
from tkinter import *

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
SECTION_SIZE = 50
SNAKE_COLOR = "green"
APPLE_COLOR = "red"
SNAKE_SPEED = 200
SECTIONS = 3
BG_COLOR = "black"

class Snake:
    def __init__(self):
        self.size = SECTIONS
        self.coordinates = []
        self.sections = []

        for i in range(0, SECTIONS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SECTION_SIZE, y + SECTION_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.sections.append(square)

class Apple:
    def __init__(self):
        x = random.randint(0, (WINDOW_WIDTH / SECTION_SIZE) - 1) * SECTION_SIZE
        y = random.randint(0, (WINDOW_HEIGHT / SECTION_SIZE) - 1) * SECTION_SIZE

        self.coordinates = [x, y]

        canvas.create_rectangle(x, y, x + SECTION_SIZE, y + SECTION_SIZE, fill = APPLE_COLOR, tag = "apple")

def play(snake, apple):
    
    x, y = snake.coordinates[0]

    if direction == "w":
        y -= SECTION_SIZE
    elif direction == "s":
        y += SECTION_SIZE
    elif direction == "a":
        x -= SECTION_SIZE
    elif direction == "d":
        x += SECTION_SIZE

    square = canvas.create_rectangle(x, y, x + SECTION_SIZE, y + SECTION_SIZE, fill = SNAKE_COLOR)

    snake.sections.insert(0, square)

    snake.coordinates.insert(0, (x, y))

    del snake.coordinates[-1]
    canvas.delete(snake.sections[-1])
    del snake.sections[-1]

    root.after(SNAKE_SPEED, play, snake, apple)

def turn():
    pass

def check_game_over():
    pass

def game_over():
    pass

root = Tk()
root.title("Snake")
root.resizable(False, False)

score = 0
direction = "s"

label = Label(root, text = "Score: {}".format(score)).pack()

canvas = Canvas(root, bg = BG_COLOR, height = WINDOW_HEIGHT, width = WINDOW_HEIGHT)
canvas.pack()

snake = Snake()
apple = Apple()

play(snake, apple)

root.mainloop()