from turtle import Turtle
import random

class Food(Turtle): 
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x,random_y)
        
    def move(self, snake):
        valid_position = False
        while not valid_position:
            random_x = random.randrange(-280, 280, 20)
            random_y = random.randrange(-280, 280, 20)
            snake_positions = [cell.pos() for cell in snake.snake_cells]
            if (random_x, random_y) not in snake_positions:
                self.goto(random_x, random_y)
                valid_position = True