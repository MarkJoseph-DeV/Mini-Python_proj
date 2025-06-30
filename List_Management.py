# This is a Python script that defines a class for managing a list of items.
# List management...
# This code implements a simple To-Do List management system.
# It allows users to add, view, remove, mark tasks as done, sort, reverse
# tasks, count tasks, find task positions, and clear all tasks.
# It uses a list to store tasks and provides a menu-driven interface for user interaction.
# The script runs in a loop until the user chooses to exit.

todo_list = [] # Initialize an empty list to store tasks

def show_menu(): # Function to display the menu options
    print('1. Add tasks')
    print('2. View tasks')
    print('3. Remove tasks')
    print('4. Mark tasks as done')
    print('5. Sort tasks')
    print('6. Reverse tasks')
    print('7. Count tasks')
    print('8. Find tasks Position')
    print('9. Clear All Tasks')
    print('10. Exit')


def add_task():         # Function to add a task to the list
    task_add = input("Enter your task: ")
    todo_list.append(task_add)
    print(f'Task "{task_add}" added to the list.')

def view_task():         # Function to view all tasks in the list
    if not todo_list:       # Check if the list is empty
        print('No Tasks in the list...')
    else:
        print('Tasks in the list:')
        for index, task in enumerate(todo_list, start=1):
            print(f'{index}. {task}')

def remove_task():       # Function to remove a task from the list
    if not todo_list:    # Check if the list is empty
        print('No tasks to remove...')
    else:
        task_to_remove = input('Enter the task to remove: ')
        if task_to_remove in todo_list: # Check if the task exists in the list
            todo_list.remove(task_to_remove)
            print(f'Task "{task_to_remove}" removed from the list...')
        else:
            print(f'Task "{task_to_remove}" not found in the list...')

def mark_task_done():   # Function to mark a task as done
    if not todo_list:   # Check if the list is empty
        print('No tasks to mark as done...')
    else:
        task_to_mark = input('Enter the task to mark as done: ')
        if task_to_mark in todo_list:   # Check if the task exists in the list
            task = todo_list.index(task_to_mark)
            todo_list[task] = f"{task_to_mark} - Done"
            print(f'Task "{task_to_mark}" marked as done.')
        else:
            print(f'"{task_to_mark}" not found in the list...')

def sort_tasks():   # Function to sort tasks in alphabetical order
    if not todo_list:
        print('No tasks to sort...')
    else:
        todo_list.sort()
        print('Tasks sorted in alphabetical order...')

def reverse_tasks():        # Function to reverse the order of tasks in the list
    if not todo_list:
        print('No tasks to reverse...')
    else:
        todo_list.reverse()
        print('Tasks reversed...')

def count_tasks():      # Function to count the number of tasks in the list
    if not todo_list:
        print('No tasks in the list...')
    else:
        print(f'Total number of tasks: {len(todo_list)}')

def find_task_position():       # Function to find the position of a task in the list
    if not todo_list:
        print('No tasks in the list...')
    else:
        task_to_find = input('Enter the task to find its position: ')
        if task_to_find in todo_list:
            position = todo_list.index(task_to_find) + 1
            print(f'Task "{task_to_find}" is at position {position}.')
        else:
            print(f'Task "{task_to_find}" not found in the list.')

def clear_all_tasks():      # Function to clear all tasks from the list
    if not todo_list:
        print('No tasks to clear...')
    else:
        todo_list.clear()
        print('All tasks cleared from the list.')

def main():     # Main function to run the To-Do List management system
    while True:
        show_menu()
        choice = input('Enter your choice (1-10): ')

        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_done()
        elif choice == '5':
            sort_tasks()
        elif choice == '6':
            reverse_tasks()
        elif choice == '7':
            count_tasks()
        elif choice == '8':
            find_task_position()
        elif choice == '9':
            clear_all_tasks()
        elif choice == '10':
            print('Exiting the program...')
            break
        else:
            print('Invalid choice, please try again.')

if __name__ == "__main__":      # Entry point of the script
    main()      