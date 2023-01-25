
FILEPATH = 'todo.txt'

def get_todos(filepath=FILEPATH): #read a text file and return the list of the todo items
    #reads a text file and return the list of todo items.
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH): #write into the todo items list in the text file
    #write the todo items in the text file
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print('hello from functions')
    print(get_todos())
