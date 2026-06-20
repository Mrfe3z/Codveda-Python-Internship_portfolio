# To‑Do App (PySide GUI)

A compact, colorful desktop To‑Do application written in Python using PySide (Qt for Python). This is an original, self-directed GUI project by the repository owner that demonstrates practical desktop app patterns — adding tasks, viewing active vs completed tasks, marking tasks complete, and deleting tasks — packaged as a friendly learning project and a polished personal portfolio piece.

Location
--------
This app lives at:
Level_2_Intermediate/Task_1_To_Do_App

Release
-------
Download pre-built packages (if available) from the repository Releases page:
https://github.com/Mrfe3z/Codveda-Python-Internship_portfolio/releases

If an executable for your platform is attached to a release, prefer that over running from source.

Screenshot
----------
<img width="402" height="732" alt="image" src="https://github.com/user-attachments/assets/ff1de723-3ef8-4b8c-822f-7187c6849822" />


About this project
------------------
- Toolkit: PySide (Qt for Python). If your code uses PySide6 specifically, replace `PySide` with `PySide6`.
- Purpose: Personal project showcasing GUI design with Qt, event handling, and task-state management.
- Scope: Simple CRUD-style task management with a two-tab interface (Active / Completed), plus UI actions for completing and deleting tasks.

Features
--------
- Add tasks using the text input and "Add Task" button
- Two tabs: Active tasks and Completed tasks
- Select a task and mark it completed to move it between tabs
- Delete tasks permanently
- Compact layout with visually distinct color styling

Requirements
------------
- Python 3.7+ (3.8+ recommended)
- PySide (PySide6 recommended) — install with pip:
  pip install PySide6
- pip install -r requirements.txt

Run from source
---------------
1. Open a terminal in this folder.
2. Launch the application. Example:
   python todo_app.py

Build a standalone executable
------------------------------
Use PyInstaller to create a single-file executable:

pip install pyinstaller
pyinstaller --onefile todo_app.py

Attach the produced binary from `dist/` to a GitHub Release for distribution.

Contributing & Improvements
---------------------------
Ideas:
- Add persistence (save/load tasks using JSON or SQLite)
- Add task metadata: due dates, priorities, or categories
- Add search/filtering and keyboard shortcuts
- Improve accessibility and keyboard focus handling

To propose changes: open an issue or submit a pull request with a description of your improvement.

License
-------
Refer to the repository root for licensing information or add a license of your choice.

Author
------
Mrfe3z
