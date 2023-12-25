from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """The ball move forward and every move is 10 to the x-coordinate and y-coordinate"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """The ball move backward, every move is -10 in y-coordinate"""
        self.y_move *= -1

    def bounce_x(self):
        """The ball move backward, every move is -10 in x-coordinate"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Set the ball to go to the center of the screen"""
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()