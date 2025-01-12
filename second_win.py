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

        self.timer1_start = False
        
        self.timer2_start = False
        

        self.timer_ss_text = QLabel(str(00))
        self.timer_ss_text.setFont(QFont('Arial',36,QFont.Bold))
        self.timer_ss_text.setHidden(True)

        self.timer3_start = False
        

        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.name_in, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age_in, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1_instruction, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1_start_btn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1_in, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2_instruction, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2_start_btn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_instruction, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_start_btn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_in_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_in_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_in_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.next_btn, alignment = Qt.AlignLeft)
        
        self.r_line.addWidget(self.timer_ss_text)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)

    #Continue here :)

    def timer_test1(self):
        self.timer1_start = True
        self.timer_ss()

    def timer_test2(self):
        self.timer2_start = True
        self.timer_ss()
    
    def timer_test3(self):
        self.timer3_start = True
        self.time = QTime(0,1,0)
        self.timer_ss_text.setText(self.time.toString('hh:mm:ss'))
        self.timer_ss_text.setFont(QFont('Arial',36,QFont.Bold))
        self.timer_ss_text.setStyleSheet('color: rgb(0,128,0)')
        self.timer_ss_text.setHidden(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3_update)
        self.timer.start(1000)
    
    def timer3_update(self):
        if self.timer3_start:
            self.time = self.time.addSecs(-1)
            self.timer_ss_text.setText(self.time.toString('hh:mm:ss'))
            if self.time.toString('hh:mm:ss') == "00:00:45":
                self.timer_ss_text.setStyleSheet('color: rgb(0,0,0)')
            if self.time.toString('hh:mm:ss') == "00:00:15":
                self.timer_ss_text.setStyleSheet('color: rgb(0,128,0)')
            if self.time.toString('hh:mm:ss') == "00:00:00":
                self.timer.stop()
                self.timer_ss_text.setHidden(True)

    def timer_ss(self):
        if self.timer1_start:
            self.count = 15
        if self.timer2_start:
            self.count = 45
        self.timer_ss_text.setText(str(self.count))
        self.timer_ss_text.setHidden(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_ss_update)
        self.timer.start(1000)

    def timer_ss_update(self):
        if self.timer1_start or self.timer2_start:
            self.count-=1
            self.timer_ss_text.setText(str(self.count))
            if self.count == 0:
                if self.timer1_start:
                    self.timer1_start = False
                    self.count = 15
                if self.timer2_start:
                    self.timer2_start = False
                    self.count = 45
                self.timer_ss_text.setHidden(True)

    def connects(self):
        self.next_btn.clicked.connect(self.next_click)
        self.test1_start_btn.clicked.connect(self.timer_test1)
        self.test2_start_btn.clicked.connect(self.timer_test2)
        self.test3_start_btn.clicked.connect(self.timer_test3)

    def calculate_index(self):
        self.p1 = int(self.test1_in.text())
        self.p2 = int(self.test3_in_1.text())
        self.p3 = int(self.test3_in_2.text())
        self.index_result = (4*(self.p1+self.p2+self.p3)-200)/10

    def index_evaluation(self):
        self.age = int(self.age_in.text())
        self.health_result = index_evaluator(self.age,self.index_result,evaluation_matrix)

    def next_click(self):
        self.calculate_index()
        self.index_evaluation()
        self.hide()
        self.fw = FinalWin(self.index_result,self.health_result)

