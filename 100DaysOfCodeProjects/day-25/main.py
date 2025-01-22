import pandas
import turtle


screen = turtle.Screen()
screen.title('US States Quiz')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


writer = turtle.Turtle()
writer.ht()
writer.penup()


states_data = pandas.read_csv('50_states.csv')


end_of_game = False


correct_guesses = 0
total_guesses = 0


states_list = states_data.state.to_list()
correct_guesses_list = []


while end_of_game != True:


    answer_state = screen.textinput(f'{total_guesses}/50 Guess the State',
                                    prompt='What is another state\'s name?').title()


    if answer_state in states_list and answer_state not in correct_guesses_list:
        x_cor = states_data[states_data.state == answer_state].x.values[0]
        y_cor = states_data[states_data.state == answer_state].y.values[0]
        writer.goto(x_cor, y_cor)
        writer.write(answer_state, align='left')
        correct_guesses_list.append(answer_state)
        correct_guesses += 1


    # DEBUG
    #print(x_cor)
    #print(y_cor)


    total_guesses += 1


    if total_guesses == 50:
        end_of_game = True


print("\nUS States Quiz")
print(f"\nScore: {correct_guesses}/{total_guesses} Correct\n")


