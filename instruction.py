from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QFont

txt_title = "Ruffier test for health"
win_x, win_y = 200,100
win_width, win_height = 1000, 600

txt_hello = "Welcome to the Health status detection program!"
txt_instruction = "The Ruffier test is a heart rate test that measures cardiorespiratory fitness (CRF).\nIt involves performing 30 squats in 45 seconds, and measuring heart rate before,\nimmediately after, and one minute after the exercise. \nThe fitness result is dependent on the age of the test-taker. \nThis test is for anyone above the age of 7."
txt_next = 'Start'

#Styling
default_font = QFont('Arial',10)
default_button = 'QPushButton{background-color:#7FFF00; border-radius: 5px; width: 160px; height: 40px; font-size:10pt;} QPushButton::hover{background-color:#32CD32} QPushButton::pressed{background-color:#006400}'

index_result = 0
performance_result = 'n/a'

txt_res1 = "low. See your doctor right away!"
txt_res2 = "satisfactory. See your doctor!"
txt_res3 = "average. It may be worth seeing your doctor to get checked out."
txt_res4 = "above average"
txt_res5 = "high"

evaluation_matrix = [['Age',txt_res1,txt_res2,txt_res3,txt_res4,txt_res5],
                     [">=15",'>=15','11-14.9','6-10.9','0.5-5.9','<=0.4'],
                     ['13-14','>=16.5','12.5-16.4','7.5-12.4','2-7.4','<=1.9'],
                     ['11-12','>=18','14-17.9','9-13.9','3.5-8.9','<=3.4'],
                     ['9-10','>=19.5','15.5-19.4','10.5-15.4','5-10.4','<=4.9'],
                     ['7-8','>=21','17-20.9','12-16.9','6.5-11.9','<=6.4']]

def index_evaluator(age,index,matrix):
    def range_to_bool(var,range):
        if '>=' in range:
            range_type = ">="
            range = var+range
            return range
        if '-' in range:
            range_splited = range.split('-')
            lower_bound = range_splited[0]
            upper_bound = range_splited[1]
            range = f'{lower_bound}<={var} and {var} <={upper_bound}'
            range_type = '-'
            return range
        if '<=' in range:
            range_type = '<='
            range = var+range
            return range
        
    if age >= 7:
        for i in range(1,len(matrix)):
            age_bool = range_to_bool('age',matrix[i][0])
            if eval(age_bool):
                age_group = i

        for n in range(1,len(matrix[age_group])):
            level_bool = range_to_bool('index',matrix[age_group][n])
            if eval(level_bool):
                level = matrix[0][n]
    
    if age <7:
        level = 'Not defined for this age.'

    return level

index_evaluator(16,5,evaluation_matrix)