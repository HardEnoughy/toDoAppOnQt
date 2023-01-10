from PySide6.QtWidgets import QMainWindow, QApplication
from ui_to_do import Ui_main_window
import sql_funcs_for_to_do_app as sql
from project import Project

class ToDoApp(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.project = Project('today')
        self.initial_state()
    
    def initial_state(self):
        text = self.project.get_tasks_texts()[0][0]
        title = self.project.get_tasks_titles()[0][0]
        self.task_title.setText(title)
        self.task_window.setText(text)
    
    def next_task(self):
        pass

    def previous_task(self):
        pass


app = QApplication()
window = ToDoApp()
window.show()
app.exec()
