from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QAction
from ui_to_do import Ui_main_window
import sql_funcs_for_to_do_app as sql
from project import Project

class ToDoApp(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = 'today'
        self.project = Project(self.name)
        self.current_id = self.project.get_first_id()
        self.show_task()

        #connecting buttons
        self.left_arrow.clicked.connect(self.previous_task)
        self.right_arrow.clicked.connect(self.next_task)
        self.done_button.clicked.connect(self.finish_task)

        #toolbar settings
        self.add_new_task_action = QAction("add new task")
        self.tool_bar.addAction(self.add_new_task_action)

        #connecting actions
        self.add_new_task_action.triggered.connect(self.open_add_task_widget)
    
    def show_task(self):
        try:
            self.name = self.project.project_list.currentText()
            self.project = Project(self.name)
            text = self.project.get_tasks_texts()[self.current_id - 1][0]
            title = self.project.get_tasks_titles()[self.current_id - 1][0]
            self.task_title.setText(title)
            self.task_window.setText(text)
        except Exception:
            print("error when trying to show task")
            self.current_id = self.project.get_first_id()
            self.show_task()
    
    def next_task(self):
        self.current_id += 1
        self.show_task()

    def previous_task(self):
        self.current_id -= 1
        self.show_task()
    
    def open_add_task_widget(self):
        self.project.show()
    
    def finish_task(self):
        sql.SqlFuncs(self.name).remove_task(self.current_id)
        self.show_task()


app = QApplication()
window = ToDoApp()
window.show()
app.exec()
