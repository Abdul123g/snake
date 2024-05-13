from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off the screen updates
screen.bgcolor("black")
screen.title("Snake Game")

food = Food()
snake = Snake()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game = True
while game:
    screen.update()
    snake.move()
    time.sleep(0.1)
    
    #gets food
    if snake.head.distance(food) < 15:
        print("collide")
        food.move(snake)
        snake.grow()
        scoreboard.increment_score()
        
    #hits wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        scoreboard.game_over()
        
    #hits tail
    if snake.tail_collision():
        game = False
        

   
    





screen.exitonclick()