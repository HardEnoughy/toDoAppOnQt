from PySide6.QtWidgets import QApplication
from toDoApp import ToDoApp

app = QApplication()
window = ToDoApp()
window.show()
app.exec()
