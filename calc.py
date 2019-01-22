import tkinter as tk
from functools import partialmethod
class Calculator:
    def __init__(self, master):
        self.master = master
        self.strvar = tk.StringVar()
        self.label = tk.Label(master, textvariable = self.strvar)
        self.master.bind('<Key>', self.keyboard_2_label)
        self.label.grid(row = 1, column = 1, columnspan = 5)
        self.master.resizable(0, 0)

        
        self.div_button = self.configure_button('/', self.print_2_label('/'), 2, 1)
        self.mul_button = self.configure_button('*', self.print_2_label('*'), 2, 2)
        self.minus_button = self.configure_button('-', self.print_2_label('-'), 2, 3)
        self.plus_button = self.configure_button('+', self.print_2_label('+'), 2, 4)
        self.zero_button = self.configure_button('0', self.print_2_label('0'), 3, 4)
        self.one_button = self.configure_button('1', self.print_2_label('1'), 3, 1)
        self.two_button = self.configure_button('2', self.print_2_label('2'), 3, 2)
        self.three_button = self.configure_button('3', self.print_2_label('3'), 3, 3)
        self.four_button = self.configure_button('4', self.print_2_label('4'), 4, 1)
        self.five_button = self.configure_button('5', self.print_2_label('5'), 4, 2)
        self.six_button = self.configure_button('6', self.print_2_label('6'), 4, 3)
        self.seven_button = self.configure_button('7', self.print_2_label('7'), 5, 1)
        self.eight_button = self.configure_button('8', self.print_2_label('8'), 5, 2)
        self.nine_button = self.configure_button('9', self.print_2_label('9'), 5, 3)
        self.nine_button = self.configure_button('(', self.print_2_label('('), 4, 5)
        self.nine_button = self.configure_button(')', self.print_2_label(')'), 5, 5)
        self.backspace_button = self.configure_button('<-', self.backspace_label(), 4, 4)
        self.clear_button = self.configure_button('DEL', self.clear_label(), 5, 4)
        self.eval_button = self.configure_button('=', self.eval_label(), 2, 6)
        self.pow_button = self.configure_button('^', self.print_2_label('^'), 3, 5)
        self.dot_button = self.configure_button('.', self.print_2_label('.'), 2, 5)
    def configure_button(self, text, command, row, column):
        button = tk.Button(self.master, text = text, command = command)
        button.grid(row = row, column = column, sticky = 'WE')
        return button
    def print_2_label(self, text):
        def _():
            nonlocal self, text
            self.strvar.set(self.strvar.get() + text)
        return _
    def backspace_label(self):
        def _():
            nonlocal self
            self.strvar.set(self.strvar.get()[:-1])
        return _
    def clear_label(self):
        def _():
            nonlocal self
            self.strvar.set('')
        return _
    def eval_label(self):
        def _():
            nonlocal self
            try:
                self.strvar.set(str(eval(self.strvar.get().replace('^', '**'))))
            except SyntaxError:
                self.strvar.set('ERROR')
        return _
    def keyboard_2_label(self, event):
        print(event)
        char = event.char
        if event.keysym == 'Return':
            self.eval_label()()
        elif  event.keysym == 'BackSpace':
            self.backspace_label()()
        elif event.keysym == 'Delete':
            self.clear_label()()
        else:
            self.print_2_label(event.char)()

if __name__ == '__main__':
    root = tk.Tk()
    c = Calculator(root)
    root.mainloop()
