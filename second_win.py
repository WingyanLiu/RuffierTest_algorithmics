from instruction import *
from final_win import FinalWin

class TestWin(QWidget):
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
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.name = QLabel('Enter Your full name:')
        self.name_in = QLineEdit('Full name')
        self.age = QLabel('Age')
        self.age_in = QLineEdit('Age in years')
        self.test1_instruction = QLabel('Lie on your back and take your pulse for 15 seconds. click the "Start the first text" button to start the timer. Write down the result in the box below.')
        self.test1_start_btn = QPushButton('Start the first test')
        self.test1_in = QLineEdit('Pulse numbers')
        self.test2_instruction = QLabel('Perform 30 squats in 45 seconds. To do this, click the "Start doing squats button to start the squat counter."')
        self.test2_start_btn = QPushButton('Start doing squats')
        self.test3_instruction = QLabel('Lie on your back and take your pulse for the first 15 seconds of the mminute, then for the last 15 seconds of the minute. \nPress the "Start final test" button to start the timer. \nThe seconds that should be measured are indicated in greene and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields.')
        self.test3_start_btn = QPushButton('Start the final test')
        self.test3_in_1 = QLineEdit('0')
        self.test3_in_2 = QLineEdit('0')
        self.next_btn = QPushButton('Send the results')

        self.l_line.addWidget(self.name)
        self.l_line.addWidget(self.name_in)
        self.l_line.addWidget(self.age)
        self.l_line.addWidget(self.age_in)
        self.l_line.addWidget(self.test1_instruction)
        self.l_line.addWidget(self.test1_start_btn)
        self.l_line.addWidget(self.test1_in)
        self.l_line.addWidget(self.test2_instruction)
        self.l_line.addWidget(self.test2_start_btn)
        self.l_line.addWidget(self.test3_instruction)
        self.l_line.addWidget(self.test3_start_btn)
        self.l_line.addWidget(self.test3_in_1)
        self.l_line.addWidget(self.test3_in_2)
        self.l_line.addWidget(self.test3_in_2)
        self.l_line.addWidget(self.next_btn)
        
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)

    #Continue here :)
    def timer_test(self):
        time = QTimer()

    def connects(self):
        self.next_btn.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = FinalWin()

