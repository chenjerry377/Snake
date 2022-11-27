from tkinter import *
import random

# define some variables for easy editing
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WINDOW_COLOR = "black"
SECTION_SIZE = 25
STARTING_SECTIONS = 3
SNAKE_COLOR = "green"
APPLE_COLOR = "red"
GAME_SPEED = 200

# creates Snake class with constructor that creates a (STARTING_SECTIONS) block long snake
class Snake:
    def __init__(self):
        self.coordinates = []
        self.sections = []
        self.length = STARTING_SECTIONS

        for i in range (0, STARTING_SECTIONS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            section = canvas.create_rectangle(x, y, x + SECTION_SIZE, y + SECTION_SIZE, fill = SNAKE_COLOR)
            self.sections.append(section)

# randomly generates an apple on the canvas upon creation
class Apple:
    def __init__(self):
        x = random.randint(0, (WINDOW_WIDTH / SECTION_SIZE) - 1) * SECTION_SIZE
        y = random.randint(0, (WINDOW_HEIGHT / SECTION_SIZE) - 1) * SECTION_SIZE

        self.coordinates = [x,y]

        apple = canvas.create_rectangle(x, y, x + SECTION_SIZE, y + SECTION_SIZE, fill = APPLE_COLOR, tag = "apple")

# method that uses Snake object and Apple object - main method
def play(snake, apple):

    x, y = snake.coordinates[0]

    if direction == "w":
        y -= SECTION_SIZE
    elif direction == "a":
        x -= SECTION_SIZE
    elif direction == "s":
        y += SECTION_SIZE
    elif direction == "d":
        x += SECTION_SIZE

    new_block = canvas.create_rectangle(x, y, x + SECTION_SIZE, y + SECTION_SIZE, fill = SNAKE_COLOR)
    snake.sections.insert(0, new_block)
    snake.coordinates.insert(0, (x,y))

    if x == apple.coordinates[0] and y == apple.coordinates[1]: # if the snake ate the apple then add 1 to score, make a new apple, and prevent 1 section of the snake from being deleted
        global score
        score += 1
        label.config(text = "Score: {}".format(score))
        canvas.delete("apple")
        apple = Apple()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.sections[-1])
        del snake.sections[-1]

    if check_game_over(snake): # checks if the snake went out of bounds or if the head hit itself
        canvas.delete(ALL)
    else:
        root.after(GAME_SPEED, play, snake, apple) # loops the game


# changes the global variable direction if the direction is not a complete 180*
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

def check_game_over(snake): # checks if the snake went off the window or if it hit itself

    x, y = snake.coordinates[0]

    if x < 0 or x >= WINDOW_WIDTH:
        return True
    elif y < 0 or y >= WINDOW_HEIGHT:
        return True

    for pairs in snake.coordinates[1:]:
        if x == pairs[0] and y == pairs[1]:
            return True

    return False

# creates tkinter window 
root = Tk()
root.title("Snake")
root.resizable(False, False)

# creates a score count at the top of the window
score = 0
label = Label(root, text = "Score: {}".format(score))
label.pack()

# declares a starting direction for the snake
direction = "s"

# creates the canvas for the game
canvas = Canvas(root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, background = WINDOW_COLOR)
canvas.pack()

# binds keys wasd so it calls the turn function with the respective key whenever the key is pressed
root.bind('<w>', lambda event: turn("w"))
root.bind('<a>', lambda event: turn("a"))
root.bind('<s>', lambda event: turn("s"))
root.bind('<d>', lambda event: turn("d"))

apple = Apple() # creates the apple and snake and then calls the main method
snake = Snake()
play(snake, apple)

root.mainloop()