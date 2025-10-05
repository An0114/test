import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, 
                               QListWidgetItem)
from PySide6.QtCore import Qt
from ui_person_info import Ui_MainWindow

class PersonInfoWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # 初始化UI
        self.setupUi(self)
        
        # 初始化单选按钮组（默认选中"男"）
        self.maleRadio.setChecked(True)
        
        # 绑定按钮事件
        self.savebtn.clicked.connect(self.save_info)
        self.restbtn.clicked.connect(self.reset_form)
        
        # 绑定菜单项事件
        # self.action_退出.triggered.connect(self.close)
        # self.action_清空.triggered.connect(self.clear_list)
        # self.action_关于.triggered.connect(self.show_about)
        
    def save_info(self):
        """保存个人信息到列表"""
        # 获取表单数据
        name = self.nameEdit.text().strip()
        age = self.ageEdit.text().strip()
        gender = "男" if self.maleRadio.isChecked() else "女"
        email = self.emailEdit.text().strip()
        intro = self.introEdit.toPlainText().strip()
        
        # 验证数据
        if not all([name, age, email]):
            QMessageBox.warning(self, "输入错误", "姓名、年龄和邮箱为必填项！")
            return
            
        if not age.isdigit():
            QMessageBox.warning(self, "输入错误", "年龄必须是数字！")
            return
            
        # 保存到列表
        info_text = f"{name} ({gender}, {age}岁) - {email}"
        item = QListWidgetItem(info_text)
        # 存储完整信息作为数据
        item.setData(Qt.UserRole, {
            "name": name,
            "age": age,
            "gender": gender,
            "email": email,
            "intro": intro
        })
        self.listWidget.addItem(item)
        
        # 提示保存成功
        QMessageBox.information(self, "成功", "信息已保存！")
        # 重置表单
        self.reset_form()
        
    def reset_form(self):
        """重置表单内容"""
        self.nameEdit.clear()
        self.ageEdit.clear()
        self.maleRadio.setChecked(True)
        self.emailEdit.clear()
        self.introEdit.clear()
        self.nameEdit.setFocus()  # 光标定位到姓名输入框
        
    def clear_list(self):
        """清空列表"""
        if self.listWidget.count() > 0:
            reply = QMessageBox.question(
                self, "确认", "确定要清空所有信息吗？",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.listWidget.clear()
                
    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(
            self, "关于", 
            "个人信息管理系统\n版本：1.0\n使用PySide6和Qt Designer开发"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PersonInfoWindow()
    window.show()
    sys.exit(app.exec())
