import turtle

robot = turtle.Turtle()
robot.shape("turtle")
robot.speed(2)

def go_forward():
    robot.forward(20)

def go_backward():
    robot.backward(20)

def turn_left():
    robot.left(30)

def turn_right():
    robot.right(30)

screen = turtle.Screen()
screen.title("Simple Robot Teleoperation Demo")
screen.listen()

screen.onkey(go_forward, "Up")
screen.onkey(go_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

turtle.done()
