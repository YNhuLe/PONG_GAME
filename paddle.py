from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=0.5)
        self.penup()
        self.goto(position)

    def go_up(self):
        """method that listen to the key to control the paddle to go up"""
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """method that listen to the key to control the paddle to go down"""
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
