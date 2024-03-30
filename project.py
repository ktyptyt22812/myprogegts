from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMessageBox,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QButtonGroup)
from random import*

logFilePath = "logs/default.txt"
app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
Buttongroup = QButtonGroup()
Buttongroup.addButton(rbtn_1)
Buttongroup.addButton(rbtn_2)
Buttongroup.addButton(rbtn_3)
Buttongroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = [
    Question('Какая обезьяна самая крупная в мире?', 'Горилла', 'бабуин', 'героин', 'шимпанзе'),
    Question('Какая из этих обезьян существует?', 'бабуин', 'дедуин', 'мамуин', 'Папуин'),
    Question('Какая из обезьян считается самым близким родственником человека?', 'шимпанзе', 'орангутан', ' горилла', 'бабуин'),
    Question('Какая из этих обезьян не человекообразная?', 'Мартышка', 'горилла', 'шимпанзе', 'орангутан'),
    Question('Какая из этих обезьян не человекообразная?', 'Мартышка', 'горилла', 'шимпанзе', 'орангутан')
]
current_question_index = 0
def ask(q: Question):
    answers = [q.right_answer, q.wrong1, q.wrong2, q.wrong3]
    shuffle(answers)
    rbtn_1.setText(answers[0])
    rbtn_2.setText(answers[1])
    rbtn_3.setText(answers[2])
    rbtn_4.setText(answers[3])
    lb_Question.setText(q.question)
    Buttongroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    Buttongroup.setExclusive(True)
def check_answer():
    selected_answer = None
    if rbtn_1.isChecked():
        selected_answer = rbtn_1.text()
    elif rbtn_2.isChecked():
        selected_answer = rbtn_2.text()
    elif rbtn_3.isChecked():
        selected_answer = rbtn_3.text()
    elif rbtn_4.isChecked():
        selected_answer = rbtn_4.text()
    correct_answer = question_list[current_question_index].right_answer
    if selected_answer == correct_answer:
        show_message("Правильно")
    else:
        show_message("Неверно")
def show_message(message):
    msg_box = QMessageBox()
    msg_box.setWindowTitle('Результат')
    msg_box.setText(message)
    msg_box.exec_()
def next_question():
    global current_question_index
    current_question_index = randint(0, 5)

    print(current_question_index)
    if current_question_index >= len(question_list):
        if current_question_index == 0:
            current_question_index = 2

        current_question_index = 0
        print(current_question_index)
    q = question_list[current_question_index]
    ask(q)
def click_ok():
    check_answer()
    btn_OK.setText('Следующий вопрос')
    next_question()
btn_OK.clicked.connect(click_ok)
window = QWidget()
layout_card = QVBoxLayout()
layout_card.addWidget(lb_Question)
layout_card.addWidget(RadioGroupBox)
layout_card.addWidget(btn_OK)
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()
initial_question = question_list[current_question_index]

ask(initial_question)
app.exec()
