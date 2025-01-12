from instruction import *

class FinalWin(QWidget):
    def __init__(self,index,result):
        super().__init__()
        self.index_result = index
        self.health_result = result
        self.set_appear()
        self.initUI()
        self.show()
        
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.index = QLabel(f'Ruffier index: {self.index_result}')
        self.index.setFont(QFont("Arial",15,QFont.Bold))
        self.index.setStyleSheet('color: rgb(0,0,205)')
        self.performance = QLabel(f'Cardiac performace: {self.health_result}')
        self.index.setFont(QFont("Arial",15,QFont.Bold))
        self.index.setStyleSheet('color: rgb(0,0,205)')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.performance, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)