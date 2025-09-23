import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QListWidgetItem)
from PySide6.QtCore import Qt
from ui_chat import Ui_Form

class chat_ui(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pubtn.clicked.connect(self.show_message)

    def show_message(self):
        msg = self.messageEdit.toPlainText().strip()
        if msg:
            self.getmessage.append(msg)
            self.messageEdit.clear()
            self.getmessage.append('''\n12311111111111111111111112312312312123123123123123123123123123123123123123123''')
        else:
            self.messageEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = chat_ui()
    window.show()
    sys.exit(app.exec_())

