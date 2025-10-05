import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QPushButton, QLineEdit,
                               QTextEdit, QSlider, QMessageBox)
from PySide6.QtCore import Qt, Signal, Slot, QEvent
from PySide6.QtGui import QFont, QIcon, QKeyEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口基本属性
        self.setWindowTitle("PySide6 界面示例")
        self.setGeometry(100, 100, 800, 600)  # x, y, 宽度, 高度

        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 添加标题
        title_label = QLabel("PySide6 界面演示")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # 添加输入区域
        input_layout = QHBoxLayout()
        input_label = QLabel("输入文本:")
        self.input_edit = QLineEdit()
        self.input_edit.setPlaceholderText("请输入内容...")
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_edit)
        main_layout.addLayout(input_layout)

        # 添加按钮
        button_layout = QHBoxLayout()
        self.show_button = QPushButton("显示内容")
        self.clear_button = QPushButton("清空")
        self.show_button.clicked.connect(self.show_text)
        self.clear_button.clicked.connect(self.clear_text)
        button_layout.addWidget(self.show_button)
        button_layout.addWidget(self.clear_button)
        main_layout.addLayout(button_layout)

        # 添加文本显示区域
        output_label = QLabel("显示区域:")
        main_layout.addWidget(output_label)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)  # 设置为只读
        main_layout.addWidget(self.output_text)

        # 添加滑块
        slider_layout = QHBoxLayout()
        slider_label = QLabel("调整字体大小:")
        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setMinimum(8)
        self.font_slider.setMaximum(24)
        self.font_slider.setValue(12)
        self.font_slider.valueChanged.connect(self.change_font_size)
        self.font_size_label = QLabel(f"当前大小: {self.font_slider.value()}")
        slider_layout.addWidget(slider_label)
        slider_layout.addWidget(self.font_slider)
        slider_layout.addWidget(self.font_size_label)
        main_layout.addLayout(slider_layout)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == Qt.Key_Return:
            self.show_text()


    def show_text(self):
        """显示输入的文本"""
        text = self.input_edit.text()
        if text:
            self.output_text.append(text)  # 添加到显示区域
            self.input_edit.clear()  # 清空输入框
        else:
            QMessageBox.warning(self, "警告", "请先输入文本内容!")

    def clear_text(self):
        """清空显示区域"""
        self.output_text.clear()

    def change_font_size(self, value):
        """改变显示区域的字体大小"""
        self.font_size_label.setText(f"当前大小: {value}")
        font = QFont()
        font.setPointSize(value)
        self.output_text.setFont(font)


if __name__ == "__main__":
    # 创建应用实例
    app = QApplication(sys.argv)

    # 创建并显示窗口
    window = MainWindow()
    window.show()

    # 进入应用主循环
    sys.exit(app.exec())
