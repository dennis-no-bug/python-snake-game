from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.create_scoreboard()

    def add_score(self):
        self.clear()
        self.total_score += 1

    def reset(self):
        self.clear()
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.total_score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.write(f"Score: {self.total_score} | High Score: {self.high_score}", False, "center", ("Arial", 15, "bold"))
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Arial", 15, "bold"))
