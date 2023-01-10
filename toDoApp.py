from PySide6.QtWidgets import QMainWindow, QApplication
from ui_to_do import Ui_main_window
import sql_funcs_for_to_do_app as sql
from project import Project

class ToDoApp(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.project = Project('today')
        self.current_id = 1
        self.show_task()

        #connecting buttons
        self.left_arrow.clicked.connect(self.previous_task)
        self.right_arrow.clicked.connect(self.next_task)
    
    def show_task(self):
        try:
            text = self.project.get_tasks_texts()[self.current_id - 1][0]
            title = self.project.get_tasks_titles()[self.current_id - 1][0]
            self.task_title.setText(title)
            self.task_window.setText(text)
        except Exception:
            print("error when trying to show task")
            self.current_id = 1
            self.show_task()
    
    def next_task(self):
        self.current_id += 1
        self.show_task()

    def previous_task(self):
        self.current_id -= 1
        self.show_task()


app = QApplication()
window = ToDoApp()
window.show()
app.exec()
