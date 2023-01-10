import MySQL_funcs
from MySQL_funcs import host_name, user_name, user_password

def create_project_table():
    query = f"""
    CREATE TABLE {project_name} (
        task_id INT PRIMARY KEY,
        task_name VARCHAR(40),
        task_text VARCHAR(2000) NOT NULL,
        date_added DATE
    );
    """
    MySQL_funcs.execute_query(connection, query)

def delete_project_table():
    query = f"""
        DROP TABLE {project_name};
    """
    MySQL_funcs.execute_query(connection, query)

def insert_task():
    task_id = input("input id: ")
    task_name = input("input name: ")
    task_text = input("input your task: ")
    # date = input("input current date: ")
    query = f"""
    INSERT INTO {project_name} VALUES
    ({task_id}, '{task_name}', '{task_text}', '2023-01-10');
    """
    MySQL_funcs.execute_query(connection, query)

def remove_task(id):
    query = f"""
    DELETE FROM {project_name}
    WHERE task_id={id}
    """
    MySQL_funcs.execute_query(connection, query)

db_name = "test_database"
connection = MySQL_funcs.create_db_connection(host_name, user_name, user_password, db_name)
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
