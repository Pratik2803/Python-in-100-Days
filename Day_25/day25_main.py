from turtle import Screen
from writer import Writer
import pandas as pd

screen = Screen()

screen.title('U.S. States')
screen.bgpic('./blank_states_img.gif')
states_information = pd.read_csv('./50_states.csv')
all_states = states_information['state'].to_list()
turtle = Writer()

already_covered_states = []


while len(already_covered_states) < 50:

    answer_state = screen.textinput(title=f"{len(already_covered_states)}/50 Correct State", prompt="Guess the state")

    if answer_state is None:
        turtle.game_over(states_guessed=len(already_covered_states))
        break

    answer_state = answer_state.title()

    answered_state_info = states_information[states_information['state'] == answer_state]

    if not answered_state_info.empty and answer_state not in already_covered_states:

        x = int(answered_state_info['x'])
        y = int(answered_state_info['y'])

        turtle.write_state(x_axies=x, y_axies=y, state_name=answer_state)
        already_covered_states.append(answer_state)


#undiscovered states

remaining_states = [state for state in all_states if state not in already_covered_states]
remaining_states_dataframe = pd.DataFrame(data=remaining_states, columns=['State'])
remaining_states_dataframe.to_csv(path_or_buf='./remaining_states.csv')

screen.exitonclick()
