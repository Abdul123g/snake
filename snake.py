from turtle import Turtle
class Snake:
    
    def __init__(self) -> None:
        self.size = 3
        self.x = 0
        self.y = 0
        self.snake_cells = []
        for i in range(self.size):
            cell = Turtle(shape="square")
            cell.color("white")
            cell.penup()
            cell.goto(self.x,self.y)
            self.snake_cells.append(cell)
            self.x -= 20
        self.head = self.snake_cells[0]
    
            
    def move(self):
        positions = [cell.pos() for cell in self.snake_cells]
        self.head.forward(20)
        for index in range(1, len(self.snake_cells)):
            self.snake_cells[index].goto(positions[index - 1])

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90) 

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270) 

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180) 

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)  

    def grow(self):
        cell = Turtle(shape="square")
        cell.color("white")
        cell.penup()
        cell.goto(self.snake_cells[-1].pos())
        self.snake_cells.append(cell)
        
def tail_collision(self):
    snake_positions = set(cell.pos() for cell in self.snake_cells[1:])
    if self.head.pos() in snake_positions:
        return True
    return False
