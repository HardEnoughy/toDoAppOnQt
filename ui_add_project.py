# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_project.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_New_project_window(object):
    def setupUi(self, New_project_window):
        if not New_project_window.objectName():
            New_project_window.setObjectName(u"New_project_window")
        New_project_window.resize(400, 300)
        self.verticalLayout = QVBoxLayout(New_project_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.project_title = QLineEdit(New_project_window)
        self.project_title.setObjectName(u"project_title")

        self.verticalLayout.addWidget(self.project_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_button = QPushButton(New_project_window)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)

        self.add_button = QPushButton(New_project_window)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(New_project_window)

        QMetaObject.connectSlotsByName(New_project_window)
    # setupUi

    def retranslateUi(self, New_project_window):
        New_project_window.setWindowTitle(QCoreApplication.translate("New_project_window", u"Form", None))
        self.cancel_button.setText(QCoreApplication.translate("New_project_window", u"PushButton", None))
        self.add_button.setText(QCoreApplication.translate("New_project_window", u"PushButton", None))
    # retranslateUi

