import turtle

# Create the game screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.setup(width=600, height=600)

# Create the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.setposition(0, 0)

# Create the food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.setposition(0, 20)

# Create the score
score = 0

# Define the game loop
while True:

    # Move the snake
    snake.forward(20)

    # Check if the snake has eaten the food
    if snake.distance(food) < 20:
        snake.dot()
        score += 1
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))

    # Check if the snake has hit the wall
    if snake.xcor() < -290 or snake.xcor() > 290 or snake.ycor() < -290 or snake.ycor() > 290:
        game_over()

    # Update the score
    wn.setworldcoordinates(-300, -300, 300, 300)
    wn.write("Score: {}".format(score), font=("Arial", 10, "bold"))

    # Check if the snake has hit itself
    for segment in snake.segments[1:]:
        if snake.distance(segment) < 20:
            game_over()

    # Delay the game
    turtle.delay(100)

# Define the game over function
def game_over():
    wn.clear()
    wn.write("Game Over", font=("Arial", 20, "bold"))
    wn.penup()
    wn.goto(0, 0)
    wn.write("Your score was: {}".format(score), font=("Arial", 10, "bold"))

# Start the game
wn.mainloop()
