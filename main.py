import turtle
import pandas

screen = turtle.Screen()
screen.title("U. S. State Game")
image = "C:/Studies/Study/python_programming/100_Day_Python/Day_26_to_30/66_us_state_game_apply_L_conprehension/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Studies/Study/python_programming/100_Day_Python/Day_26_to_30/66_us_state_game_apply_L_conprehension/50_states.csv")
all_states = data.state.to_list()

guessed_state_list = []
while len(guessed_state_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state_list)}/50", prompt="What's another stat's name?").title()
    
    if answer_state == "Exit":
        # using list comprehension
        missing_states = [state for state in all_states if state not in guessed_state_list]
        # for state in all_states:
        #     if state not in guessed_state_list:
        #         missing_states.append(state)
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_state_file.csv")
        break

    if answer_state in all_states:
        guessed_state_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()  # No need this function because use mainloop()