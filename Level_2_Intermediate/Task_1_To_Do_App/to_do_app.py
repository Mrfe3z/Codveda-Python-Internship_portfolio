import json

options = '''1. Add Task
2. Delete Task 
3. mark as done
4. list tasks
5. Q to quit'''

try:
    with open('tasks.json', 'r', encoding='UTF-8') as file:
        save_data = json.load(file)

        task_list = save_data['active_tasks']
        completed_tasks = save_data['completed_tasks']

except FileNotFoundError:
    task_list = []
    completed_tasks = []


def save_tasks():

    save_data = {
        'active_tasks': task_list,
        'completed_tasks': completed_tasks
    }
    # Dump the whole dictionary into the file
    with open('tasks.json', 'w', encoding='UTF-8') as file:
        json.dump(save_data, file, indent=4)


while True:
    print(options)
    user_choice = input('select an option\n>> ')

    if user_choice == str(5) or user_choice == 'Q'.lower():
        print('Goodbye, see you next task!')
        break

    try:
        user_choice = int(user_choice)
    except ValueError as e:
        print('please enter a valid option(numbers only)')
        continue

    if user_choice == 1:
        task_name = input('what task would you like to add:\n>> ')
        task_list.append(task_name)
        save_tasks()

    elif user_choice == 2:
        count = 1
        for task in task_list:
            print(f'{count}. {task}')
            count += 1

        del_option = input('select task to delete ')
        try:
            del_option = int(del_option)
        except ValueError as e:
            print('please enter a valid option(numbers only)')
            continue

        if (del_option-1) >= len(task_list) or (del_option-1) < 0:
            print('please select from the available tasks')
            continue

        del task_list[del_option-1]
        print('task deleted successfully')
        save_tasks()

    elif user_choice == 3:
        count = 1
        for task in task_list:
            print(f'{count}. {task}')
            count += 1
        completion_option = input('select task to mark as completed\n>> ')
        try:
            completion_option = int(completion_option)
        except ValueError as e:
            print('please enter a valid option(numbers only)')
            continue

        if (completion_option-1) >= len(task_list) or (completion_option-1) < 0:
            print('please select from the available tasks')
            continue

        completed_task = task_list.pop(int(completion_option)-1)
        completed_tasks.append(completed_task)
        save_tasks()

    elif user_choice == 4:
        print('\n--- ACTIVE TASKS ---')
        if len(task_list) == 0:
            print("  No active tasks yet!")
        else:
            count = 1
            for task in task_list:
                print(f'  {count}. {task}')
                count += 1

        print('\n--- COMPLETED TASKS ---')
        if len(completed_tasks) == 0:
            print("  Nothing completed yet. Get to work!")
        else:
            for task in completed_tasks:
                print(f'  {task}✌️')

        print('\n')
        continue
