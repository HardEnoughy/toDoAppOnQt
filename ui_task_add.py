# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_add.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_add_task_widget(object):
    def setupUi(self, add_task_widget):
        if not add_task_widget.objectName():
            add_task_widget.setObjectName(u"add_task_widget")
        add_task_widget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(add_task_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.project_list = QComboBox(add_task_widget)
        self.project_list.setObjectName(u"project_list")

        self.verticalLayout.addWidget(self.project_list)

        self.task_title = QLineEdit(add_task_widget)
        self.task_title.setObjectName(u"task_title")
        self.task_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.task_title)

        self.task_text_edit = QTextEdit(add_task_widget)
        self.task_text_edit.setObjectName(u"task_text_edit")

        self.verticalLayout.addWidget(self.task_text_edit)

        self.buttons_h_layout = QHBoxLayout()
        self.buttons_h_layout.setObjectName(u"buttons_h_layout")
        self.cancel_button = QPushButton(add_task_widget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.buttons_h_layout.addWidget(self.cancel_button)

        self.add_button = QPushButton(add_task_widget)
        self.add_button.setObjectName(u"add_button")

        self.buttons_h_layout.addWidget(self.add_button)


        self.verticalLayout.addLayout(self.buttons_h_layout)


        self.retranslateUi(add_task_widget)

        QMetaObject.connectSlotsByName(add_task_widget)
    # setupUi

    def retranslateUi(self, add_task_widget):
        add_task_widget.setWindowTitle(QCoreApplication.translate("add_task_widget", u"Form", None))
        self.cancel_button.setText(QCoreApplication.translate("add_task_widget", u"Cancel", None))
        self.add_button.setText(QCoreApplication.translate("add_task_widget", u"Add", None))
    # retranslateUi

