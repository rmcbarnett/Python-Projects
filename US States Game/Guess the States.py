# This game (based on the Turtle module) allows you to guess the names of states in the US.  Right answers are placed on the map.
# Score is also updated.



import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
import time


def create_turtle(x,y,answer_state):
    turtle_answer = turtle.Turtle()
    turtle_answer.hideturtle()
    turtle_answer.penup()
    turtle_answer.goto(x, y)
    turtle_answer.write(answer_state)


data = pandas.read_csv('./50_states.csv')
print(data)
States = data["state"].tolist()

answer_state = screen.textinput(title="Guess the State",prompt="Whats another states name")
score = 0

screen.tracer(0)
state_list = []
y_list = []
x_list = []

game_is_on = True
while game_is_on:
    answer_state = answer_state.title()
    print(answer_state)
    if answer_state =="Exit":
        for state in States:
            state_row= data[data["state"] == state]
            state_list.append(state_row.state.item())
            y_list.append(int(state_row.y))
            x_list.append(int(state_row.x))
        new_data = {"State":state_list,'x':x_list,'y':y_list}
        df = pandas.DataFrame(new_data)
        df.to_csv('./States to learn.csv')

        break


    if answer_state in States:
        score +=1
        state_coordinates = data[data['state']== answer_state]
        print(state_coordinates)
        x = int(state_coordinates.x)
        y = int(state_coordinates.y)
        create_turtle(x,y,answer_state)
        time.sleep(.1)
        screen.update()
        States.remove(answer_state)
    # if result:
    #     state_coordinates = States.index(answer_state)
    # print(result)


    answer_state = screen.textinput(title=f'Score{score}/50', prompt="Whats another states name")
    if score == 50:
        game_is_on == True
        "Congrats!! You got all, Baby!"



#
# screen.exitonclick()
