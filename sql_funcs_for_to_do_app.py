import MySQL_funcs
from MySQL_funcs import host_name, user_name, user_password

db_name = "to_do_app_database"

class SqlFuncs():
    def __init__(self, name):
        self.project_name = name
        self.connection = MySQL_funcs.create_db_connection(host_name, user_name, user_password, db_name)
        
    def create_project_table(self):
        query = f"""
        CREATE TABLE {self.project_name} (
            task_id INT PRIMARY KEY,
            task_name VARCHAR(40),
            task_text VARCHAR(2000) NOT NULL,
            date_added DATE
        );
        """
        MySQL_funcs.execute_query(self.connection, query)

    def delete_project_table(self):
        query = f"""
            DROP TABLE {self.project_name};
        """
        MySQL_funcs.execute_query(self.connection, query)

    def insert_task(self, task_id, task_name, task_text):
        # task_id = input("input id: ")
        # task_name = input("input name: ")
        # task_text = input("input your task: ")
        # date = input("input current date: ")
        query = f"""
        INSERT INTO {self.project_name} VALUES
        ({task_id}, '{task_name}', '{task_text}', '2023-01-10');
        """
        MySQL_funcs.execute_query(self.connection, query)

    def remove_task(self, id):
        query = f"""
        DELETE FROM {self.project_name}
        WHERE task_id={id}
        """
        MySQL_funcs.execute_query(self.connection, query)
    
    def get_all_rows(self):
        query = f"""
        SELECT * FROM {self.project_name}
        """
        return(MySQL_funcs.read_query(self.connection, query))
    
    def get_projects_names(self):
        query = f"""
        SHOW TABLES;
        """
        return(MySQL_funcs.read_query(self.connection, query))
    
    def get_id(self):
        query = f"""
        SELECT task_id FROM {self.project_name}
        ORDER BY task_id DESC
        """
        return(MySQL_funcs.read_query(self.connection, query))
    
    def get_text(self):
        query = f"""
        SELECT task_text FROM {self.project_name}
        """
        return(MySQL_funcs.read_query(self.connection, query))
    
    def get_title(self):
        query = f"""
        SELECT task_name FROM {self.project_name}
        """
        return(MySQL_funcs.read_query(self.connection, query))

# sql = SqlFuncs("today")
# sql.insert_task()

"""
project_name = input("write your project name: ") 
action = input("choose func: delete, insert, remove or create: ")
if action == 'delete':
    delete_project_table()
elif action == 'create':
    create_project_table() 
elif action == 'insert':
    insert_task()
elif action == 'remove':
    id = input("input id: ")
    remove_task(id)
else:
    print("wrong input")
"""
