import turtle
import pandas

# Read state data from CSV
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

# Create turtle screen and load image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle to write the state names
state_writer = turtle.Turtle()
state_writer.hideturtle()
state_writer.penup()

guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter the next state").title()

    if answer == "Exit":
        # Find missing states
        missing_states = [state for state in state_list if state not in guessed_states]
        print(missing_states)
        break

    if answer in state_list and answer not in guessed_states:
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        state_writer.goto(int(state_data.x), int(state_data.y))
        state_writer.write(answer, align="center", font=("Arial", 8, "normal"))
