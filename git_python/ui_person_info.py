# -*- coding: utf-8 -*-

################################################################################

##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 500)
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.actioncopy = QAction(MainWindow)
        self.actioncopy.setObjectName(u"actioncopy")
        self.actionzhantie = QAction(MainWindow)
        self.actionzhantie.setObjectName(u"actionzhantie")
        self.actionqingkong = QAction(MainWindow)
        self.actionqingkong.setObjectName(u"actionqingkong")
        self.actionguanyu = QAction(MainWindow)
        self.actionguanyu.setObjectName(u"actionguanyu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 601, 431))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.name = QLabel(self.widget)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)

        self.nameEdit = QLineEdit(self.widget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 3)

        self.listwidget = QListWidget(self.widget)
        self.listwidget.setObjectName(u"listwidget")

        self.gridLayout.addWidget(self.listwidget, 0, 4, 5, 1)

        self.age = QLabel(self.widget)
        self.age.setObjectName(u"age")

        self.gridLayout.addWidget(self.age, 1, 0, 1, 1)

        self.egeEdit = QLineEdit(self.widget)
        self.egeEdit.setObjectName(u"egeEdit")

        self.gridLayout.addWidget(self.egeEdit, 1, 1, 1, 3)

        self.sex = QLabel(self.widget)
        self.sex.setObjectName(u"sex")

        self.gridLayout.addWidget(self.sex, 2, 0, 1, 1)

        self.maleRadio = QRadioButton(self.widget)
        self.maleRadio.setObjectName(u"maleRadio")

        self.gridLayout.addWidget(self.maleRadio, 2, 1, 1, 1)

        self.famelRadio = QRadioButton(self.widget)
        self.famelRadio.setObjectName(u"famelRadio")

        self.gridLayout.addWidget(self.famelRadio, 2, 2, 1, 2)

        self.email = QLabel(self.widget)
        self.email.setObjectName(u"email")

        self.gridLayout.addWidget(self.email, 3, 0, 1, 1)

        self.emailEdit = QLineEdit(self.widget)
        self.emailEdit.setObjectName(u"emailEdit")

        self.gridLayout.addWidget(self.emailEdit, 3, 1, 1, 3)

        self.person = QLabel(self.widget)
        self.person.setObjectName(u"person")

        self.gridLayout.addWidget(self.person, 4, 0, 1, 1)

        self.personEdit = QTextEdit(self.widget)
        self.personEdit.setObjectName(u"personEdit")

        self.gridLayout.addWidget(self.personEdit, 4, 1, 1, 3)

        self.savebtn = QPushButton(self.widget)
        self.savebtn.setObjectName(u"savebtn")

        self.gridLayout.addWidget(self.savebtn, 5, 0, 1, 1)

        self.restbtn = QPushButton(self.widget)
        self.restbtn.setObjectName(u"restbtn")

        self.gridLayout.addWidget(self.restbtn, 5, 1, 1, 2)

        self.seltn = QPushButton(self.widget)
        self.seltn.setObjectName(u"seltn")

        self.gridLayout.addWidget(self.seltn, 5, 3, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionnew)
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionexit)
        self.menu_2.addAction(self.actioncopy)
        self.menu_2.addAction(self.actionzhantie)
        self.menu_2.addAction(self.actionqingkong)
        self.menu_3.addAction(self.actionguanyu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u4fe1\u606f\u7ba1\u7406\u7cfb\u7edf", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.actioncopy.setText(QCoreApplication.translate("MainWindow", u"copy", None))
        self.actionzhantie.setText(QCoreApplication.translate("MainWindow", u"zhantie", None))
        self.actionqingkong.setText(QCoreApplication.translate("MainWindow", u"qingkong", None))
        self.actionguanyu.setText(QCoreApplication.translate("MainWindow", u"guanyu", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.age.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84", None))
        self.sex.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None))
        self.maleRadio.setText(QCoreApplication.translate("MainWindow", u"\u7537", None))
        self.famelRadio.setText(QCoreApplication.translate("MainWindow", u"\u5973", None))
        self.email.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1", None))
        self.person.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u7b80\u4ecb", None))
        self.savebtn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.restbtn.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.seltn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6&F", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

