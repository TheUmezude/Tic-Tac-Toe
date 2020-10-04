from IPython.display import clear_output


# Create a program that allows a user to replace values in an array, in a lean way as possible

# Function that displays the array
def display_array(the_array, the_array1, the_array2):
    clear_output()
    print('Current game: ')
    print(f'{the_array[0]}  |  {the_array[1]}  |  {the_array[2]}')
    print('---|-----|---')
    print(f'{the_array1[0]}  |  {the_array1[1]}  |  {the_array1[2]}')
    print('---|-----|---')
    print(f'{the_array2[0]}  |  {the_array2[1]}  |  {the_array2[2]}')

    #print(the_array)
    #print(the_array1)
    #print(the_array2)


# Function that asks for and validates user array choice to modify the array
def user_input():
    choice = 'WRONG'
    game_play = False

    while choice.isdigit() is False or game_play is False:
        choice = input('Please select an unselected spot (1 - 9): \n')

        if choice.isdigit() is True:
            if int(choice) in range(1, 10):
                game_play = True
            else:
                game_play = False

    return int(choice)


# Function to check available game spots
def check_game(the_array, the_array1, the_array2, spot_value):

    while spot_value in range(1, 10):
        actual_value = spot_value - 1
        actual_value1 = spot_value - 4
        actual_value2 = spot_value - 7

        if spot_value in [1, 2, 3]:
            if the_array[actual_value] not in ['X', 'x', 'O', 'o']:
                return True
            else:
                return False
        elif spot_value in [4, 5, 6]:
            if the_array1[actual_value1] not in ['X', 'x', 'O', 'o']:
                return True
            else:
                return False
        elif spot_value in [7, 8, 9]:
            if the_array2[actual_value2] not in ['X', 'x', 'O', 'o']:
                return True
            else:
                return False


# Function that appends arrays
def append_function(the_array, the_array1, the_array2, spot_value, letter):
    actual_value = spot_value - 1
    actual_value1 = spot_value - 4
    actual_value2 = spot_value - 7

    if spot_value in [1, 2, 3]:
        the_array[actual_value] = letter
    elif spot_value in [4, 5, 6]:
        the_array1[actual_value1] = letter
    elif spot_value in [7, 8, 9]:
        the_array2[actual_value2] = letter


# Function to check X/O input
def x_o_entry():
    selected = 'hdvbvbu'

    while selected not in ['x', 'X', 'o', 'O']:
        selected = input('You have to input either X or O: ')

    if selected in ['x', 'X']:
        selected = 'X'
    elif selected in ['o', 'O']:
        selected = 'O'

    return selected


# Function to check winner of game
def check_winner(the_array, the_array1, the_array2):
    #Vertical from first column
    if the_array[0] == the_array1[0] and the_array1[0] == the_array2[0]:
        print(f'***The person with the {the_array[0]} wins!***')
        return 'end'
    #Vertical from second column
    elif the_array[1] == the_array1[1] and the_array1[1] == the_array2[1]:
        print(f'***The person with the {the_array[1]} wins!***')
        return 'end'
    #Vertical from third column
    elif the_array[2] == the_array1[2] and the_array1[2] == the_array2[2]:
        print(f'***The person with the {the_array[2]} wins!***')
        return 'end'
    #Horizontal from first row
    elif the_array[0] == the_array[1] and the_array[1] == the_array[2]:
        print(f'***The person with the {the_array[0]} wins!***')
        return 'end'
    #Horizontal from second row
    elif the_array1[0] == the_array1[1] and the_array1[1] == the_array1[2]:
        print(f'***The person with the {the_array1[0]} wins!***')
        return 'end'
    #Horizontal from third row
    elif the_array2[0] == the_array2[1] and the_array2[1] == the_array2[2]:
        print(f'***The person with the {the_array2[0]} wins!***')
        return 'end'
    #Diagonal from first column and row
    elif the_array[0] == the_array1[1] and the_array1[1] == the_array2[2]:
        print(f'***The person with the {the_array[0]} wins!***')
        return 'end'
    #Diagonal from third column and first row
    elif the_array[2] == the_array1[1] and the_array1[1] == the_array2[0]:
        print(f'***The person with the {the_array[2]} wins!***')
        return 'end'

    #else:
     #   print('Sadly, no one wins this round!')
      #  return 'end'



# Function that allows users break out of the game
def continue_game():
    answer = 'Nofhbrh'

    while answer not in ['yes', 'Yes', 'Y', 'No', 'no', 'N']:
        answer = input('Would you like to play again (Y/N)? \n')

    if answer in ['Yes', 'yes', 'Y', 'y']:
        answer = 'Y'
    elif answer in ['No', 'no', 'N', 'n']:
        print('That\'s alright, goodbye for now!')
        answer = 'N'

    return answer


# General code sequence
in_game = True
#game_sequence = True
response = 67
response1 = 'gang'
escape = 'rjnrjg'


while in_game is True:
    my_array1 = [1, 2, 3]
    my_array2 = [4, 5, 6]
    my_array3 = [7, 8, 9]
    print('\n\n***************************************')
    print('Hello! Welcome to my Tic-Tac-Toe!')
    display_array(my_array1, my_array2, my_array3)
    game_sequence = True

    while game_sequence is True:
        print('Please select a shelf to modify!')
        response = user_input()

        if check_game(my_array1, my_array2, my_array3, response) is False:
            response = user_input()

        response1 = x_o_entry()
        append_function(my_array1, my_array2, my_array3, response, response1)

        if my_array1[0] in ['X', 'x', 'O', 'o'] and my_array1[1] in ['X', 'x', 'O', 'o'] and my_array1[2] in ['X', 'x', 'O', 'o']:
            if my_array2[0] in ['X', 'x', 'O', 'o'] and my_array2[1] in ['X', 'x', 'O', 'o'] and my_array2[2] in ['X', 'x', 'O', 'o']:
                if my_array3[0] in ['X', 'x', 'O', 'o'] and my_array3[1] in ['X', 'x', 'O', 'o'] and my_array3[2] in ['X', 'x', 'O', 'o']:
                    game_sequence = False

        display_array(my_array1, my_array2, my_array3)

        final_check = check_winner(my_array1, my_array2, my_array3)

        if final_check == 'end':
            break

    if final_check == 'end':
        play_again = continue_game()

    if play_again == 'Y':
        in_game = True
    elif play_again == 'N':
        in_game = False