import json


class TaskManager:
    def __init__(self):
        try:
            with open('tasks.json', 'r', encoding='UTF-8') as file:
                content = json.load(file)

                self.active_tasks_lists = content['active_tasks']
                self.completed_tasks_lists = content['completed_tasks']
        except FileNotFoundError as e:
            self.active_tasks_lists = []
            self.completed_tasks_lists = []

    def add_tasks(self, task):
        if task.strip() == '':
            return False
        self.active_tasks_lists.append(task)
        self.save_tasks()
        return True

    def del_tasks(self, index):
        index = int(index)
        if index >= len(self.active_tasks_lists) or len(self.active_tasks_lists) == 0:
            return None
        del self.active_tasks_lists[index]
        self.save_tasks()

    def mark_completed_tasks(self, index):
        if index >= len(self.active_tasks_lists) or len(self.active_tasks_lists) == 0:
            return None
        comp = self.active_tasks_lists.pop(index)
        self.completed_tasks_lists.append(comp)
        self.save_tasks()

    def save_tasks(self):
        save_data = {'active_tasks': self.active_tasks_lists,
                     'completed_tasks': self.completed_tasks_lists}

        with open('tasks.json', 'w') as file:
            json.dump(save_data, file, indent=4)
