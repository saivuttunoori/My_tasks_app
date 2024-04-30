FP = "tasks.txt"


def get_tasks(filepath=FP):
    """"reads the file and shows the items"""
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FP):
    """writes the new tasks in the file"""
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)
