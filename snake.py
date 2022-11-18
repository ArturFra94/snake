import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates



#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Score
scoretext = turtle.Turtle()
scoretext.speed(0)
scoretext.color("white")
scoretext.penup()
scoretext.hideturtle()
'''score.clear()
turtle.clear()'''
scoretext.goto(0, 260)
'''s = len(segments)
score.write(f"Score:{s} ", font=('Times New Roman',15))'''
scoretext.write("Score:  0  High Score: 0",align="center", font=("Times New Roman",20,"normal"))

def clear():
    scoretext.clear()

#fuctions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
# keyboard binding
wn.listen() # zczytanie z klawiatury
wn.onkeypress(go_up, "w") #gdy nacisnę w, wywołaj funkcje paddle_a_up
wn.onkeypress(go_down, "s") #gdy nacisnę s, wywołaj funkcje paddle_a_up
wn.onkeypress(go_right, "d") #gdy nacisnę d, wywołaj funkcje paddle_a_up
wn.onkeypress(go_left, "a") #gdy nacisnę a, wywołaj funkcje paddle_a_up
wn.onkeypress(clear, 'c')


'''wn.listen() # zczytanie z klawiatury
wn.onkeypress(head.direction, "8") #gdy nacisnę y, wywołaj funkcje paddle_a_up
wn.onkeypress(head.direction, "5") #gdy nacisnę y, wywołaj funkcje paddle_a_up
wn.onkeypress(paddle_b_up, "w") #gdy nacisnę y, wywołaj funkcje paddle_a_up
wn.onkeypress(paddle_b_down, "s") #gdy nacisnę y, wywołaj funkcje paddle_a_up
'''
#Main game loop
while True:
    wn.update()
    #checking distance
    if head.distance(food) < 20:
        x= random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        #przypisanie listy do segmentu
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 1

        if score > high_score:
            high_score = score
        scoretext.clear()
        scoretext.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                    font=("Times New Roman", 20, "normal"))




    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
    # listy zaczynają się od 0, więc trzeba -1, drugi argument to na czym liczenie ma sie skończyć
# a trzeci oznacza o ile ma się zmniejszać odliczanie
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    #border checking
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # clear the segment list
        segments.clear()

        # reset the score
        score = 0
        scoretext.clear()
        scoretext.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                        font=("Times New Roman", 20, "normal"))

        # reset delay
        delay = 0.1

    move()

    # body coliisions
    for segment in segments:
        if segment.distance(head) < 20:
            wn.bgcolor("red")
            time.sleep(2)
            wn.bgcolor("green")
            head.goto(0,0)
            head.direction="stop"
            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segment list
            segments.clear()
            score = 0
            scoretext.clear()
            scoretext.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                    font=("Times New Roman", 20, "normal"))

            # reset delay
            delay = 0.1
    time.sleep(delay)
wn.mainloop()