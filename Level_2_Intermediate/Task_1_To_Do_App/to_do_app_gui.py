# from PySide6.QtGui import QScreen
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
                               QPushButton, QVBoxLayout, QWidget, QMainWindow, QLabel, QTabWidget)
from PySide6.QtCore import QSize, Qt

from color_widget import Color, QColor
import sys
import json

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        try:
            with open('tasks.json', 'r', encoding='UTF-8') as file:
                save_data = json.load(file)

                self.active_tasks_lists = save_data['active_tasks']
                self.completed_tasks_lists = save_data['completed_tasks']
        except FileNotFoundError:
            self.active_tasks_lists = []
            self.completed_tasks_lists = []

# window settings
        self.setWindowTitle('TO-DO APP')
        self.setPalette(QColor(''))

        # window sizes
        self.setFixedSize(QSize(400, 700))

# All button widgets
        # add button settings
        self.add_button = QPushButton('Add Task')
        self.add_button.setFixedHeight(60)
        self.add_button.setPalette(QColor('green'))

        # delete button settings
        self.del_button = QPushButton('Delete Task')
        self.del_button.setPalette(QColor('red'))
        self.del_button.setFixedSize(120, 60)

        self.active_tasks_widget = QListWidget()
        self.completed_tasks_widget = QListWidget()

        for task in self.active_tasks_lists:
            self.active_tasks_widget.addItem(task)

        for task in self.completed_tasks_lists:
            self.completed_tasks_widget.addItem(task)

        # text input field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('add a new task')
        self.input_field.setFixedSize(QSize(300, 60))

        self.complete_task_button = QPushButton('Mark Completed')
        self.complete_task_button.setFixedSize(120, 60)
        self.complete_task_button.setPalette(QColor('blue'))

# all buttons signal
        # add button
        self.add_button.clicked.connect(self.add_tasks)
        # delete button
        self.del_button.clicked.connect(self.delete_tasks)
        # completed tasks button
        self.complete_task_button.clicked.connect(self.completed_task)


# layout settings
        # App orientation
        page_layout = QVBoxLayout()

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.North)
        self.tab_widget.addTab(self.active_tasks_widget, 'active tasks')
        self.tab_widget.addTab(self.completed_tasks_widget, 'completed tasks')

        # add andtext field orientation
        layout_1 = QHBoxLayout()
        layout_1.addWidget(self.input_field)
        layout_1.addWidget(self.add_button)

        layout_2 = QHBoxLayout()
        layout_2.addWidget(self.complete_task_button,
                           alignment=Qt.AlignmentFlag.AlignLeft)

        page_layout.addLayout(layout_1)
        page_layout.addWidget(self.tab_widget)

        page_layout.addLayout(layout_2)

        layout_2.addWidget(
            self.del_button, alignment=Qt.AlignmentFlag.AlignRight)

# background (not screen)
        dummy_widget = QWidget()
        dummy_widget.setLayout(page_layout)

        self.setCentralWidget(dummy_widget)


# slots

    def add_tasks(self):
        # print('clicked add button')
        task_name = self.input_field.text()
        if task_name.strip() == '':
            return
        self.active_tasks_lists.append(task_name)
        # update the visible list immediately
        self.active_tasks_widget.addItem(task_name)
        self.input_field.clear()
        self.save_tasks()

    def delete_tasks(self):
        row = self.active_tasks_widget.currentRow()
        if row < 0:
            return  # nothing selected
        del self.active_tasks_lists[row]
        self.active_tasks_widget.takeItem(row)
        self.save_tasks()

    def completed_task(self):
        row = self.active_tasks_widget.currentRow()
        if row < 0:
            return  # nothing selected

        # remove from active data, get the task name back
        completed_task_name = self.active_tasks_lists.pop(row)
        # add it to completed data
        self.completed_tasks_lists.append(completed_task_name)

        # remove from active widget
        self.active_tasks_widget.takeItem(row)
        # add to completed widget
        self.completed_tasks_widget.addItem(completed_task_name)

        self.save_tasks()

    def save_tasks(self):
        save_data = {
            'active_tasks': self.active_tasks_lists,
            'completed_tasks': self.completed_tasks_lists
        }
        # Dump the whole dictionary into the file
        with open('tasks.json', 'w', encoding='UTF-8') as file:
            json.dump(save_data, file, indent=4)


window = MainWindow()
window.show()
app.exec()
