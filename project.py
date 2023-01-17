from PySide6.QtWidgets import QWidget, QApplication
from ui_task_add import Ui_add_task_widget
from task import Task
import sql_funcs_for_to_do_app as sql

class Project(QWidget, Ui_add_task_widget):
    """This class manages projects tables and also setting up task add window"""
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.data = sql.SqlFuncs(name)
        self.last_id = self.get_last_id()
        self.setup_project_list()

        #connecting buttons
        self.cancel_button.clicked.connect(self.exit)
        self.add_button.clicked.connect(self.add_task)
    
    def get_tasks_texts(self):
        return(self.data.get_text())

    def get_tasks_titles(self):
        return(self.data.get_title())
    
    def get_last_id(self):
        id = self.data.get_id()
        return id[0][0] if id else 0
    
    def get_first_id(self):
        id = self.data.get_id()
        return id[-1][0] if id else 0
    
    def setup_project_list(self):
        """give to combo box task titles"""
        projects = self.data.get_projects_names()
        print(projects)
        for project in projects:
            self.project_list.addItem(project[0])
    
    def exit(self):
        self.close()
    
    def add_task(self):
        """sends info to task class for adding to database"""
        task_name = self.task_title.text()
        task_text = self.task_text_edit.toPlainText()
        self.name = self.project_list.currentText()
        if task_name and task_text:
            self.last_id += 1
            task = Task(self.last_id, task_name, task_text, self.name)
            task.add_to_database()
            self.close()
    

# app = QApplication()
# project = Project("today")
# project.show()
# app.exec()
