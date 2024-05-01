import time
from turtle import Screen, Turtle
from snake import Snake  # convert to OOP
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background colour
screen.title("My Snake Game")  # title of game at the top bar
screen.tracer(0)  # stop screen from refreshing


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()  # listen for keystroke
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()  # Refresh screen
    time.sleep(0.1)  # update every 0.1 sec
    snake.move()

    # Detect collision with food, with distance method
    if snake.head.distance(food) < 15:  # if less than 15 to the food, accounting of buffer for food size
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        score.reset()
        snake.reset()


    # Detect collision with tail
    # for segment in snake.segments:
    #     if segment == snake.head:  # ensure it does not immediately loses
    #         pass
    #     elif snake.head.distance(segment) < 10:  # distance wrt any part of the snake
    #         game_is_on = False
    #         score.game_over()

    # Detect collision with tail via slicing , slicing [start : stop : step], eg [::2], whole list but increase by 2
    for segment in snake.segments[1:]:  # slicing to exclude the head, : and empty after to signal all the way to end of list
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score.reset()
            snake.reset()


screen.exitonclick()
