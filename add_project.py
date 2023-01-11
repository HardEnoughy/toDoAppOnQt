from PySide6.QtWidgets import QWidget
from ui_add_project import Ui_New_project_window
from sql_funcs_for_to_do_app import SqlFuncs

class NewProject(QWidget, Ui_New_project_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #connecting buttons
        self.cancel_button.clicked.connect(self.exit)
        self.add_button.clicked.connect(self.add_new_project)
    
    def exit(self):
        self.close()
    
    def add_new_project(self):
        text = self.project_title.text()
        if text:
            sql = SqlFuncs(self.project_title.text())
            sql.create_project_table()
            self.close()
