# from PySide6.QtGui import QScreen
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
                               QPushButton, QVBoxLayout, QWidget, QMainWindow, QLabel, QTabWidget)
from PySide6.QtCore import QSize, Qt

from task_manager import TaskManager
from color_widget import Color, QColor
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.manager = TaskManager()

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

        for task in self.manager.active_tasks_lists:
            self.active_tasks_widget.addItem(task)

        for task in self.manager.completed_tasks_lists:
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
        if not self.manager.add_tasks(task_name):
            return  # manager rejected it (e.g. blank input) — do nothing
        self.active_tasks_widget.addItem(task_name)
        self.input_field.clear()

    def delete_tasks(self):
        row = self.active_tasks_widget.currentRow()
        if row < 0:
            return  # nothing selected
        self.manager.del_tasks(row)
        self.active_tasks_widget.takeItem(row)

    def completed_task(self):
        row = self.active_tasks_widget.currentRow()
        if row < 0:
            return  # nothing selected
        completed_name = self.manager.mark_completed_tasks(row)
        if completed_name is None:
            return  # manager rejected it (shouldn't normally happen here)
        self.active_tasks_widget.takeItem(row)
        self.completed_tasks_widget.addItem(completed_name)
