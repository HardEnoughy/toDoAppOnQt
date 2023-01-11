# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'to_do.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(746, 485)
        self.main_layout = QWidget(main_window)
        self.main_layout.setObjectName(u"main_layout")
        self.horizontalLayout_5 = QHBoxLayout(self.main_layout)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.projects_tab = QVBoxLayout()
        self.projects_tab.setObjectName(u"projects_tab")
        self.today = QPushButton(self.main_layout)
        self.today.setObjectName(u"today")

        self.projects_tab.addWidget(self.today)


        self.horizontalLayout_5.addLayout(self.projects_tab)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.task_title = QLineEdit(self.main_layout)
        self.task_title.setObjectName(u"task_title")
        self.task_title.setAlignment(Qt.AlignCenter)
        self.task_title.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.task_title)

        self.tasks_overview_widget = QWidget(self.main_layout)
        self.tasks_overview_widget.setObjectName(u"tasks_overview_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.tasks_overview_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.left_arrow = QPushButton(self.tasks_overview_widget)
        self.left_arrow.setObjectName(u"left_arrow")

        self.horizontalLayout_4.addWidget(self.left_arrow)

        self.task_window = QTextEdit(self.tasks_overview_widget)
        self.task_window.setObjectName(u"task_window")
        self.task_window.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.task_window)

        self.right_arrow = QPushButton(self.tasks_overview_widget)
        self.right_arrow.setObjectName(u"right_arrow")

        self.horizontalLayout_4.addWidget(self.right_arrow)


        self.verticalLayout_4.addWidget(self.tasks_overview_widget)

        self.done_button = QPushButton(self.main_layout)
        self.done_button.setObjectName(u"done_button")

        self.verticalLayout_4.addWidget(self.done_button)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        main_window.setCentralWidget(self.main_layout)
        self.tool_bar = QToolBar(main_window)
        self.tool_bar.setObjectName(u"tool_bar")
        self.tool_bar.setMinimumSize(QSize(0, 20))
        self.tool_bar.setMovable(False)
        main_window.addToolBar(Qt.TopToolBarArea, self.tool_bar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.today.setText(QCoreApplication.translate("main_window", u"Today", None))
        self.left_arrow.setText(QCoreApplication.translate("main_window", u"PushButton", None))
        self.right_arrow.setText(QCoreApplication.translate("main_window", u"PushButton", None))
        self.done_button.setText(QCoreApplication.translate("main_window", u"Done", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("main_window", u"toolBar", None))
    # retranslateUi

