# To display score
from turtle import Turtle
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_highscore.txt") as data:
            self.high_score = int(data.read())  # opening file
        self.hideturtle()
        self.speed("fastest")
        self.sety(280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("snake_highscore.txt", mode="w") as data: # help to save data every time code is rerun
            data.write(str(self.high_score))