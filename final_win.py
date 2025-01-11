from instruction import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.index = QLabel(f'Ruffier index:{index_result}')
        self.performance = QLabel(f'Cardiac performace:{performance_result}')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.performance, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)