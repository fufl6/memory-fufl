#создай приложение для запоминания информации
from random import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
layout_main = QVBoxLayout
asdf = QPushButton('где же ковбой')

ghjk = QLabel('стоять ковбой')
RadioGroupBox = QGroupBox('Варианты')
btn_answer1 = QRadioButton('Да')
btn_answer2 = QRadioButton('ковбой нагетс')
btn_answer3 = QRadioButton('сам стой')
btn_answer4 = QRadioButton('у меня пропали штаны')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

oh2 = QHBoxLayout()
oh2.addWidget(ghjk)
oh1 = QHBoxLayout()
oh1.addWidget(RadioGroupBox)
oh3 = QHBoxLayout()
oh3.addWidget(asdf)


og1 = QVBoxLayout()
og1.addLayout(oh2)
og1.addLayout(oh1)

GroupBox = QButtonGroup()
GroupBox.addButton(btn_answer1)
GroupBox.addButton(btn_answer2)
GroupBox.addButton(btn_answer3)
GroupBox.addButton(btn_answer4)

AnsGroupBox = QGroupBox('результат')
RadioGroupBox.hide()
AnsGroupBox.show()
ogf1 = QLabel('Да')
ogf2 = QLabel('IQ100/IQ0')
mogf1 = QVBoxLayout()
mogf1.addWidget(ogf2)
mogf1.addWidget(ogf1, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(mogf1)
og1.addWidget(AnsGroupBox)
def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    asdf.setText('дальше ковбой')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    asdf.setText('вперёд ковбой')
    GroupBox.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    GroupBox.setExclusive(True)
def test():
    if asdf.text() == 'вперёд ковбой':
        show_results()
    else:
        show_question()

answer = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def show_correct(res):
    ogf2.setText(res)
    show_results()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        if answer[1].isChecked() or answer[2].isChecked or answer[3].isChecked:
            show_correct('Неправильно')



class Question():
    def __init__(self, question, right_answer, wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    ghjk.setText(q.question)
    ogf1.setText(q.right_answer)
    show_question()
q = Question('вопрос', 'Да','сам стой','у меня пропали штаны','ковбой нагетс')
ask(q)
vopros_list = []
q1 = Question('i been',
'married long time ago', 'chocolad',
'pelmen', 'da')
vopros_list.append(q1)
q2 = Question('cotton',
'eye joe', 'candy', 'da', 'zamok')
vopros_list.append(q2)
q3 = Question('where',
'you come from', 'meth', 'da', 'kluch')
vopros_list.append(q3)
q4 = Question ('gedi',
'dage', 'dugi','da','dolgi')
vopros_list.append(q4)
q5 = Question ('сколько км прошёл гг dl2 перед тем как попал в старый Виледор',
'2000','1500','2100','3000')
vopros_list.append(q5)
q6 = Question ('заражён ли гг dl2?',
 'да','нет','не знаю','он мёртв')
vopros_list.append(q6)
q7 = Question ('Кого ищёт гг dl2',
 'сестру','маму','собаку','друга должника ')
vopros_list.append(q7)
q8 = Question ('как называется организация по разработке вакцины в dl2?',
'ВГМ','МДП','ОРН','ОПРВ')
vopros_list.append(q8)
q9 = Question ('кто спас гг dl2 когда он попал на базар?',
'Хакон','Лоан','Джек','Мия')
q10 = Question ('какая фракция разлила химикаты в Виледоре?',
'Ревенаты','Миротворцы','Жители','Сам гг')
vopros_list.append(q10)


def next_question():
    main_win.total += 1
    cur_question = randint(0, len(vopros_list) - 1)
    q = vopros_list[cur_question]
    ask(q)
    print('Статистика' , '\n -Всего вопросов:' , main_win.total ,'\n-Правильных ответов:' ,main_win.score ,'\n Рейтинг:' , main_win.score/main_win.total * 100)








main_win.cur_question = -1

def click_OK():
    if asdf.text() == 'вперёд ковбой':
        check_answer()
    else:
        next_question()

asdf.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0


og1.addLayout(oh3)
main_win.setLayout(og1)
main_win.show()
app.exec_()