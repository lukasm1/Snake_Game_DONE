from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def create_frame(self):
        self.goto(-290, -290)
        self.pendown()
        self.setheading(0)
        self.pensize(2)
        self.pendown()
        self.forward(580)
        self.setheading(90)
        self.forward(580)
        self.setheading(180)
        self.forward(580)
        self.setheading(270)
        self.forward(580)
        self.penup()
        self.goto(0, 290)

    def update_scoreboard(self):
        self.clear()
        self.create_frame()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
