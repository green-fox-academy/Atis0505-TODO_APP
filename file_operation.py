todo_list = "todo_list.txt"

def get_list():
    return read_file(todo_list)


def add_to_list(task_name):
    try:
        with open(todo_list, "a") as file:
            file.write("[ ], " + task_name)
    except IOError:
        print("Unable to write file: ",todo_list)
    return get_list()


def remove_from_list(index):
    return get_list()


def complete_task(index):
    return get_list()


def read_file(todo_list):
    try:
        file = open(todo_list,"r")
        my_file = file.readlines()
        if len(my_file) == 0:
            return print("No todos for today!")
        else:
            for line in my_file:
                print(line.rstrip())
            file.close()
    except IOError:
        print("Unable to read file: ",todo_list)