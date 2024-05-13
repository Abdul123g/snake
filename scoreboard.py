from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.hideturtle()
        self.penup()  # Ensure no drawing when moving
        self.goto(0, 280)  # Move the scoreboard to a visible location
        self.write_score()

    def write_score(self):
        self.clear()  # Clear the previous score
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 10, "normal"))

    def increment_score(self):
        self.score += 1
        self.write_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))
