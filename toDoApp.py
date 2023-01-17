from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtGui import QAction
from ui_to_do import Ui_main_window
import sql_funcs_for_to_do_app as sql
from project import Project
from add_project import NewProject

class ToDoApp(QMainWindow, Ui_main_window):
    """main window class"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = 'today'
        self.project = Project(self.name)
        self.index = 0
        self.projects_list = ['today']
        self.show_task()
        self.refresh_project_tab()
        self.current_id = 1

        #connecting buttons
        self.left_arrow.clicked.connect(self.previous_task)
        self.right_arrow.clicked.connect(self.next_task)
        self.done_button.clicked.connect(self.finish_task)
        self.today.clicked.connect(self.change_current_project)

        #toolbar settings
        self.add_new_task_action = QAction("add new task")
        self.tool_bar.addAction(self.add_new_task_action)
        self.add_new_project_action = QAction("add new project")
        self.tool_bar.addAction(self.add_new_project_action)
        self.refresh_projects_action = QAction("refresh projects")
        self.tool_bar.addAction(self.refresh_projects_action)
        self.delete_project_action = QAction("delete current project")
        self.tool_bar.addAction(self.delete_project_action)

        #connecting actions
        self.add_new_task_action.triggered.connect(self.open_add_task_widget)
        self.add_new_project_action.triggered.connect(self.create_new_project)
        self.refresh_projects_action.triggered.connect(self.refresh_project_tab)
        self.delete_project_action.triggered.connect(self.delete_project)
    
    def print_something(self):
        print("Some sort of griberish")
    
    def delete_project(self):
        """removes table from database"""
        if self.name != 'today':
            data = sql.SqlFuncs(self.name)
            data.delete_project_table()
            self.projects_list.remove(self.name)
            self.name = 'today'
            self.refresh_project_tab()
            self.show_task()
    
    def show_task(self):
        """shows tasks if there is any"""
        try:
            self.project = Project(self.name)
            text = self.project.get_tasks_texts()[self.index][0]
            title = self.project.get_tasks_titles()[self.index][0]
            self.task_title.setText(title)
            self.task_window.setText(text)
        except Exception:
            print("error when trying to show task")
            self.current_id = self.project.get_first_id()
            self.index = 0
            try:
                text = self.project.get_tasks_texts()[self.index]
                self.show_task()
            except:
                self.show_blank_page()
    
    def next_task(self):
        """calls next task if there is any"""
        self.index += 1
        self.show_task()

    def previous_task(self):
        """calls previous task if there is any"""
        self.index -= 1
        self.show_task()
    
    def open_add_task_widget(self):
        """add task window"""
        self.project.show()
    
    def finish_task(self):
        """removes task from database"""
        titles = self.project.get_tasks_titles()
        self.current_id = sql.SqlFuncs(self.name).get_one_id(titles[self.index][0])[0][0]
        print(self.current_id)
        sql.SqlFuncs(self.name).remove_task(self.current_id)
        self.show_task()
    
    def show_blank_page(self):
        """blank page if there is no tasks"""
        self.task_title.setText('')
        self.task_window.setText('')
    
    def create_new_project(self):
        """creates new table"""
        self.window = NewProject()
        self.window.show() 
    
    def refresh_project_tab(self):
        """adding new buttons(if there is any) on project list"""
        projects = sql.SqlFuncs(self.name).get_projects_names()
        if len(projects) > 1:
            for i in range(0, len(projects)):
                if projects[i][0] in self.projects_list:
                    continue
                button = QPushButton(projects[i][0])
                self.projects_tab.addWidget(button)
                button.clicked.connect(self.change_current_project)
                self.projects_list.append(projects[i][0])
    
    def change_current_project(self):
        """changes table"""
        button = self.sender()
        self.name = button.text().lower()
        self.show_task()
