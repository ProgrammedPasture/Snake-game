
from turtle import Turtle

ALIGN = "center"
FONT = ("Times New Roman", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("my_file.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align= ALIGN, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_file.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def snake_scores(self):
        self.score +=1
        self.update_scoreboard()

