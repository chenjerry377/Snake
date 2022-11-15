import random
from tkinter import *

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
SECTION_SIZE = 50
SNAKE_COLOR = "green"
APPLE_COLOR = "red"
SNAKE_SPEED = 1000
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

    if x == apple.coordinates[0] and y == apple.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("apple")
        apple = Apple()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.sections[-1])
        del snake.sections[-1]

    if check_game_over(snake):
        game_over()
    else:
        root.after(SNAKE_SPEED, play, snake, apple)
    
def turn(new_direction):
    global direction

    if new_direction == "w":
        if direction != "s":
            direction = new_direction
    if new_direction == "a":
        if direction != "d":
            direction = new_direction
    if new_direction == "d":
        if direction != "a":
            direction = new_direction
    if new_direction == "s":
        if direction != "w":
            direction = new_direction

def check_game_over(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= WINDOW_WIDTH:
        return(True)
    elif y < 0 or y >= WINDOW_HEIGHT:
        return(True)

    for coords in snake.coordinates[1:]:
        if x == coords[0] and y == coords[1]:
            return(True)

    return(False)

def game_over():
    canvas.delete(ALL)

root = Tk()
root.title("Snake")
root.resizable(False, False)

score = 0
direction = "s"

label = Label(root, text = "Score: {}".format(score))
label.pack()

canvas = Canvas(root, bg = BG_COLOR, height = WINDOW_HEIGHT, width = WINDOW_HEIGHT)
canvas.pack()

root.bind('<Left>', lambda event: turn("a"))
root.bind('<Right>', lambda event: turn("d"))
root.bind('<Up>', lambda event: turn("w"))
root.bind('<Down>', lambda event: turn("s"))

snake = Snake()
apple = Apple()

play(snake, apple)

root.mainloop()