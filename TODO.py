import sys
from options_menu import print_options
import file_operation

user_input = sys.argv

def check_user_input(us_input):
    if len(us_input) == 1:
        return print_options()
    elif len(us_input) == 2:
        return action_operator(us_input[1], "")
    elif len(us_input) == 3:
        return action_operator(user_input[1], us_input[2])
    
    
def action_operator(us_com, user_string):
    if us_com == "-l":
        file_operation.get_list()
    elif us_com == "-a":
        file_operation.add_to_list(user_string)
    elif us_com == "-r":
        file_operation.remove_from_list(int(user_string))
    elif us_com == "-c":
        file_operation.complete_task(int(user_string))
    else:
        return print("Use expected keys!")

check_user_input(user_input)
