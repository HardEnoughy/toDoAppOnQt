import sql_funcs_for_to_do_app as sql

class Task():
    """class for task management"""
    def __init__(self, id, name, text, project):
        self.task_id = id
        self.task_name = name
        self.task_text = text
        self.project = project
        self.data = sql.SqlFuncs(project)
    
    def add_to_database(self):
        self.data.insert_task(self.task_id, self.task_name, self.task_text)
        