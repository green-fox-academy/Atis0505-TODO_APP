todo_data = "todo_data.txt"

def get_list():
    line_text = ""
    dict_list = create_dict_for_file()
    for index, dict_item in enumerate(dict_list):
        line_text += str(index+1) + " - "
        if dict_item["complete"] == False:
            line_text += "[ ] "
        else:
            line_text += "[X] "
        line_text += dict_item["task_name"]
    print(line_text)

def get_len_of_file():
    dict_list = create_dict_for_file()
    len_number = len(dict_list)
    return len_number


def add_to_list(task_name):
    dict_list = create_dict_for_file()
    dict_list[-1]["task_name"] = dict_list[-1]["task_name"][0:]+"\n"
    todo_dict = {}
    todo_dict["complete"] = False
    todo_dict["task_name"] = task_name
    dict_list.append(todo_dict)
    save_file(dict_list)


def remove_from_list(index):
    dict_list = create_dict_for_file()
    del dict_list[index-1]
    save_file(dict_list)


def complete_task(index):
    dict_list = create_dict_for_file()
    dict_list[index-1]["complete"] = True
    save_file(dict_list)


def create_dict_for_file():
    todo_list = []
    file = open(todo_data, "r")
    my_file = file.readlines()
    for line in my_file:
        todo_dict = {}
        if line[0] == "0":
            todo_dict["complete"] = False
        else:
            todo_dict["complete"] = True
        task_name_text = line[2:]
        todo_dict["task_name"] = task_name_text
        todo_list.append(todo_dict)
    return todo_list
    file.close()


def save_file(new_list):
    line_text = "" 
    with open(todo_data, "w") as f:
        for line in new_list:
            if line["complete"]:
                line_text += '1 '
            else:
                line_text += "0 "
            line_text += line["task_name"]
            f.writelines(line_text)
            line_text = ""
    return get_list()