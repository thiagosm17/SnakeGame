from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.largest_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.largest_score}", False, "center", font=('Courier', 24, 'normal'))

    def game_over(self):
        if self.largest_score < self.score:
            self.largest_score = self.score
            self.update_scoreboard()
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", font=('Courier', 30, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()