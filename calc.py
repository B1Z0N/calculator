#!/usr/bin/python3
import re
import sys

from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QDesktopWidget
    )

from form import Ui_Form


class Calculator(QWidget, Ui_Form):
    def update(self):
        return self.display.setText(str(self.exprstr))

    def addsym(self, sym):
        self.exprstr += str(sym)
        self.update()

    def _eval(self):
        if len(self.exprstr) > 0:
            try:
                self.exprstr = str(eval(self.exprstr))
                self.display.setText(self.exprstr)
            except:
                self.display.setText(':ERR:')
            self.exprstr = ''

    def dellast(self):
        self.exprstr = self.exprstr[:(len(self.exprstr) - 1)]
        self.update()

    def dellall(self):
        self.exprstr = ''
        self.display.setText('0')

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.validSymbols = re.compile(r'[^\d\-\+\.\/\*\^\(\)]')
        self.exprstr = ''

        # centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        addsym = self.addsym
        dellast = self.dellast
        dellall = self.dellall
        _eval = self._eval

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

    def keyPressEvent(self, event):
        char = event.text()
        key = event.key()
        if self.validSymbols.search(char) == None:
            self.addsym(char)
        if key == 16777220:
            self._eval()
        elif key == 16777219:
            self.dellast()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    calc = Calculator()
    sys.exit(app.exec())
