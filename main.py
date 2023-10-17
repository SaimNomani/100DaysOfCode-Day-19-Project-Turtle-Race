from turtle import Turtle, Screen
import turtle
import random
# screen setup
screen=Screen()
screen.bgcolor('black')
screen.setup(width=500, height=400)
screen.title('Turtle Race')
#
turtles=[]
no_of_turtles=5
colors=['red','blue', 'green','yellow','purple']
def generate_turtle(x_cordinate, y_cordinate):
    """function to generate turtle on their respective position"""
    for i in range(0,no_of_turtles):
        turTle=Turtle(shape='turtle')
        turtles.append(turTle)
        turTle.color(colors[i])
        turTle.penup()
        turTle.goto(x=x_cordinate, y=y_cordinate)
        y_cordinate-=50
def move():
    """generate random motion of each turtle."""
    for turTle in turtles:
        turTle.forward(random.randint(1,5))
def check_win():
    """To check which turtle reaches the finish line first and return its index"""
    for i in range(no_of_turtles):
        if turtles[i].xcor()>230:
            return i
    return -1
def play():
    x_cord=-230
    y_cord=100
    user_bet=(screen.textinput(title='Make Your Bet', prompt='Which turtle(red, green, blue, purple, yellow) will win  the race? Enter a color')).lower()
    print(f"User's choice: {user_bet}")
    # generate heading at center
    turtle_heading=Turtle()
    turtle_heading.penup()
    turtle_heading.goto(0,screen.window_height()/2-40)
    turtle_heading.pendown()
    turtle_heading.hideturtle()
    turtle_heading.pencolor('red')
    turtle_heading.write("TURTLE RACE", align='center', font=('Arial',20,'bold'))
    #
    generate_turtle(x_cordinate=x_cord, y_cordinate=y_cord)
    while True:
        move()
        win=check_win()
        if win != -1:
            # Generate the game result text.
            turtle_heading.clear()
            turtle_text = Turtle()
            turtle_text.penup()
            turtle_text.pendown()
            turtle_text.hideturtle()
            turtle_text.pencolor('red')
            #
            if user_bet==colors[win]:
                print(f"you've won!! The {colors[win]} turtle is the winner")
                turtle_text.write(f"you've won\n{colors[win]} turtle wins", align='center', font=('Arial', 20, 'bold'))
            else:
                print(f"you've lost!! The {colors[win]} turtle is the winner")
                turtle_text.write(f"you've lost!!\n{colors[win]} turtle wins", align='center', font=('Arial', 20, 'bold'))
            break
    for i in range(no_of_turtles):
        # final positions of each turtle at the end of the race
        print(f"{colors[i]}: x={turtles[i].xcor()} y={turtles[i].ycor()}")
        #
    # winner
    print(f"winner: {colors[win]}\n-----------------------------------------")
    #
    play_again=screen.textinput(title="Play Again", prompt="Type 'y' to play again or 'n' to exit")
    if play_again=='y':
        # restarting the game
        turtles.clear()
        screen.reset()
        play()
    elif play_again=='n':
        # closing the window
        screen.bye()
play()



