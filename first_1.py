from function import get_todos, write_todos
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It's now", now)
while True:

    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith("show"):

        todos = get_todos()

        # new_todos =[item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')

            row = f"{index + 1}-{item}"

            print(row)

    elif user_action.startswith('edit'):
        try:

            number = int(user_action[5:])
            print(number)
            number = number-1

            todos = get_todos()

            print('here is todos existing', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("enter the valid index")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid.")

print("Bye")
