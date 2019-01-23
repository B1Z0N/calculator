#!/usr/bin/python3
import sys
from form import Ui_Form
from PyQt5.QtGui import (
    QWindow,
)

from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QDesktopWidget
)


class Calculator(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exprstr = ''

        # centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        update = lambda: self.display.setText(str(self.exprstr))


        def addsym(sym):
            self.exprstr += str(sym)
            update()

        def _eval():
            try:
                self.exprstr = str(eval(self.exprstr))
            except:
                self.display.setText(':ERR:')
                self.exprstr = ''
            # self.exprstr = str(eval(self.exprstr))
            # update()

        def dellast():
            self.exprstr = self.exprstr[:(len(self.exprstr) - 1)]
            update()

        def dellall():
            self.exprstr = ''
            self.display.setText('0')
    
        self.one.clicked.connect(lambda: addsym(1))
        self.two.clicked.connect(lambda: addsym(2))
        self.three.clicked.connect(lambda: addsym(3))
        self.four.clicked.connect(lambda: addsym(4))
        self.five.clicked.connect(lambda: addsym(5))
        self.six.clicked.connect(lambda: addsym(6))
        self.seven.clicked.connect(lambda: addsym(7))
        self.eight.clicked.connect(lambda: addsym(8))
        self.nine.clicked.connect(lambda: addsym(9))
        self.zero.clicked.connect(lambda: addsym(0))

        self.del_last.clicked.connect(dellast)

        self.plus.clicked.connect(lambda: addsym('+'))
        self.minus.clicked.connect(lambda: addsym('-'))
        self.div_btn.clicked.connect(lambda: addsym('/'))
        self.mul.clicked.connect(lambda: addsym('*'))
        self.right_bracket.clicked.connect(lambda: addsym(')'))
        self.left_bracket.clicked.connect(lambda: addsym('('))
        self.pow.clicked.connect(lambda: addsym('^'))
        self.dot.clicked.connect(lambda: addsym('.'))

        self.pushButton_9.clicked.connect(_eval)

        self.deletebtn.clicked.connect(dellall)


app = QApplication(sys.argv)

calc = Calculator()
calc.show()
sys.exit(app.exec())
