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
        return action_operator(us_input[1], us_input[2])
    elif len(us_input) >= 3:
        task_name_string = ""
        for i in range(2,len(us_input)):
            task_name_string += us_input[i]+" "
        return action_operator(us_input[1], task_name_string)
    
    
def action_operator(us_com, user_string):
    if us_com == "-l":
        file_operation.get_list()
    elif us_com == "-a":
        if user_string == "":
            print("Unable to add: no task provided")
        else:
            file_operation.add_to_list(user_string)
    try:
        if user_string == "":
            return print("Unable to remove: no index provided")
        if (int(user_string)) > file_operation.get_len_of_file():
            return print("Unable to remove: index is out of bound")
        else:      
            if us_com == "-r":
                file_operation.remove_from_list(int(user_string))
            elif us_com == "-c":
                file_operation.complete_task(int(user_string))  
    except ValueError:
        return print("Unable to remove: index is not a number")    
    else:
        return print("Unsupported argument!\n")
        print_options()
        

check_user_input(user_input)
