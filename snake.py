from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
      self.bodies = []
      self.create_snake()
      self.head = self.bodies[0]
     
    
    def create_snake(self):
         self.new_x = 0
         for _ in range(0,3):
            self.new_x -= 20
            self.add_segment(self.new_x)
          

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setx(self.new_x)
        self.bodies.append(new_segment)

    def extend(self):
        self.add_segment(self.bodies[-1].position())

    def move(self):
        for seg_num in range(len(self.bodies) - 1, 0, -1):
            new_x_pos = self.bodies[seg_num - 1].xcor()
            new_y_pos = self.bodies[seg_num - 1].ycor()
            self.bodies[seg_num].goto(new_x_pos, new_y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
      

 
        
