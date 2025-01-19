from instruction import *
from second_win import TestWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)

        self.hello_text.setFont(QFont('Arial', 15, QFont.Bold)) 
        self.instruction.setFont(QFont('Arial', 10))
        self.button.setStyleSheet('QPushButton{background-color:lightblue; border-radius: 5px; width: 150px; height: 50px; font-size:16pt;} QPushButton::pressed{background-color:grey}')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
app.setFont(default_font) 
app.setStyleSheet(default_button)
mw = MainWin()
app.exec_()
