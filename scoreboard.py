from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        file = open("HighScore.txt", mode="r")
        self.score = 0
        self.high_score = int(file.read())
        file.close()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False, "center", font=('Courier', 24, 'normal'))

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            file = open("HighScore.txt", mode="w")
            file.write(str(self.high_score))
            file.close()


        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

