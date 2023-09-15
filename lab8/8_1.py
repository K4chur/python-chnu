from tkinter import *
from tkinter.messagebox import *
import math

root = Tk()
root.minsize(width=350, height=150)
root.maxsize(width=800, height=300)
root.title("Калькулятор")

fr_xy = Frame(root, bg="black")
fr_xy.pack(side=TOP, expand=YES, fill=X)
fr_xy.config(cursor="hand2")

lx = Label(fr_xy, text="x =", bg="black", fg="white")
lx.pack(side=LEFT, padx=10, pady=10)

entX = Entry(fr_xy, bg="black", fg="white")
entX.insert(0, 0)
entX.pack(side=LEFT, padx=10, pady=10)
entX.focus()

ly = Label(fr_xy, text="y =", bg="black", fg="white")
ly.pack(side=LEFT, padx=10, pady=10)

entY = Entry(fr_xy, bg="black", fg="white")
entY.insert(0, 0)
entY.pack(side=LEFT, padx=10, pady=10)

fr_op = LabelFrame(root, text="Операция:", bg="black", fg="white")
fr_op.pack(side=TOP, expand=YES, fill=X)

# Добавьте операции "sqrt(x)" и "y^2" в список oper
oper = ['+', '−', '∗', '/', '%', '//', 'sqrt(x)', 'y^2']
varOper = StringVar()

for op in oper:
    Radiobutton(fr_op, text=op, variable=varOper, value=op, bg="black", fg="white").pack(side=LEFT, padx=20, pady=10)

varOper.set(oper[0])

fr_res = Frame(root, bg="black")
fr_res.pack(side=TOP, expand=YES, fill=BOTH)


def OnButtonResult():
    try:
        x = float(entX.get())
    except ValueError:
        showerror("Ошибка ввода", "Переменная x не является числом")
        return

    try:
        y = float(entY.get())
    except ValueError:
        showerror("Ошибка ввода", "Переменная y не является числом")
        return

    op = varOper.get()

    if op == '+':
        res = x + y
    elif op == '−':
        res = x - y
    elif op == '∗':
        res = x * y
    elif op == '/':
        if y != 0:
            res = x / y
        else:
            res = 'NAN'
    elif op == '%':
        res = x % y
    elif op == '//':
        if y != 0:
            res = x // y
        else:
            res = 'NAN'
    elif op == 'sqrt(x)':  # Обработка операции "корень квадратный из x"
        if x >= 0:
            res = math.sqrt(x)
        else:
            res = 'NAN'
    elif op == 'y^2':  # Обработка операции "квадрат y"
        res = y ** 2
    else:
        res = 'Операция выбрана неверно'

    lres['text'] = res


Button(fr_res, text="=", width=10, command=OnButtonResult, cursor="hand2").pack(side=LEFT, padx=30, pady=20)
lres = Label(fr_res, text="", bg="black", fg="white")
lres.pack(side=LEFT, padx=30, pady=20)

root.mainloop()
