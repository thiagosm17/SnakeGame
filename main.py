from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

high_score = open("HighScore.txt")


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()




    if snake.snake[0].distance(food) < 15:
        food.ramdomizer()
        snake.extend()
        scoreboard.increase_score()

    if snake.snake[0].xcor() >= 280 or snake.snake[0].xcor() <= -280 or snake.snake[0].ycor() >= 280 or snake.snake[
        0].ycor() <= -280:
        snake.reset()
        scoreboard.reset()


    for segs in snake.snake[1:]:
        if snake.snake[0].distance(segs) < 10:
            snake.reset()
            scoreboard.reset()

high_score.close()

screen.exitonclick()