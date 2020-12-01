
from tkinter import *
import array as arr


def openbrac():
    global s
    s = s+'('
    s1.set(s)
    return


def closedbrac():
    global s
    s = s+')'
    s1.set(s)
    return


def clear():
    global s
    global top
    global c
    global x
    s = s.replace(s, "")
    top = -1
    c = c.replace(c, "")
    x = []
    s1.set('0')
    answer.set('0')
    return


def delete():
    global s
    s = s[:-1]
    s1.set(s)
    return


def num7():
    global s
    s = s+'7'
    s1.set(s)
    return


def num8():
    global s
    s = s+'8'
    s1.set(s)
    return


def num9():
    global s
    s = s+'9'
    s1.set(s)
    return


def num4():
    global s
    s = s+'4'
    s1.set(s)
    return


def num5():
    global s
    s = s+'5'
    s1.set(s)
    return


def num6():
    global s
    s = s+'6'
    s1.set(s)
    return


def num1():
    global s
    s = s+'1'
    s1.set(s)
    return


def num2():
    global s
    s = s+'2'
    s1.set(s)
    return


def num3():
    global s
    s = s+'3'
    s1.set(s)
    return


def num0():
    global s
    s = s+'0'
    s1.set(s)
    return


def plus():
    global s
    s = s+'+'
    s1.set(s)
    return


def minus():
    global s
    s = s+'-'
    s1.set(s)
    return


def div():
    global s
    s = s+'/'
    s1.set(s)
    return


def mul():
    global s
    s = s+'*'
    s1.set(s)
    return


def power():
    global s
    s = s+'^'
    s1.set(s)
    return


def point():
    global s
    s = s+'.'
    s1.set(s)
    return


def solve():
    global s
    global top
    s = s
    s1.set(s)

    def ischar(a1):
        if a1 == '+' or a1 == '-' or a1 == '*' or a1 == '/' or a1 == '^' or a1 == '(':
            return True
        return False

    def isnum(a2):
        if a2 == '+' or a2 == '-' or a2 == '*' or a2 == '/' or a2 == '^':
            return False
        return True

    def con(w):
        return float(w)

    def cal(a3, b1, c1):
        if c1 == '+':
            return a3+b1
        if c1 == '-':
            return a3-b1
        if c1 == '*':
            return a3*b1
        if c1 == '/':
            if b1 == 0:
                answer.set("Invalid! Press clear to continue")
            return a3/b1
        return a3 ** b1

    def pre(a4):
        if a4 == '+' or a4 == '-':
            return 1
        if a4 == '*' or a4 == '/':
            return 2
        if a4 == '^':
            return 3
        return 4

    def push(v):
        global top
        global c
        top = top+1
        c = c+v
        return

    def pop():
        global c
        global top
        c = c[:-1]
        top = top-1
        return

    def push1(u):
        global top
        global x
        top = top+1
        x.insert(top, u)
        return

    def pop1():
        global top
        global x
        if top < 0:
            return -1
        l = x[top]
        x = x[:-1]
        top = top-1
        return l

    def peek():
        if top == -1:
            return -1
        return c[top]

    j = 0
    n = len(s)
    b = []
    x1 = ""
    for i in range(0, n):
        if ischar(s[i]):
            if x1 != "":
                b.append(x1)
                j = j+1
                x1 = x1.replace(x1, "")
            g = pre(s[i])
            if top != (-1):
                h = pre(peek())
                while top != (-1) and h >= g and peek() != '(':
                    b.append(peek())
                    j = j+1
                    pop()
                    h = pre(peek())
            push(s[i])
        elif s[i] == ')':
            if x1 != "":
                b[j] = x1
                j = j+1
                x1 = x1.replace(x1, "")
            if top != (-1):
                while top != (-1) and peek() != '(':
                    b.append(peek())
                    j = j+1
                    pop()
                if peek() != '(':
                    print("Invalid")
                else:
                    pop()
            else:
                print("Invalid")
                break
        else:
            x1 += s[i]
    if x1 != "":
        b.append(x1)
        j = j+1
    while top != (-1):
        b.append(peek())
        pop()
        j = j+1
    top = (-1)
    for i in range(0, j):
        if isnum(b[i]):
            j = con(b[i])
            push1(j)
        else:
            g1 = pop1()
            h = pop1()
            push1(cal(h, g1, b[i]))
    answer.set(str(pop1()))
    s1.set(s)
    return


root = Tk()
top = -1
c = ""
x = arr.array('d', [])
y = " "
s = ""
root.title(160*y+"CALCULATOR")
s1 = StringVar()
s1.set("0")
answer = StringVar()
answer.set("0")
entry1 = Entry(root, textvariable=s1)
entry1.grid(row=0, columnspan=5, ipady=16, ipadx=40)
entry1.config(font=("Verdana", 15))
label1 = Label(root, text="Result")
label1.grid(row=1, column=0)
label1.config(font=("Verdana", 15))
label2 = Label(root, textvariable=answer)
label2.grid(row=1, columnspan=4, ipady=16, ipadx=20)
label2.config(font=("Verdana", 15))
btn1 = Button(root, text="(", command=openbrac, bg='yellow', fg='black', height=4, width=8)
btn1.grid(row=2, column=0)
btn1.config(font=("Verdana", 15))
btn2 = Button(root, text=")", command=closedbrac, bg='yellow', fg='black', height=4, width=8)
btn2.grid(row=2, column=1)
btn2.config(font=("Verdana", 15))
btn3 = Button(root, text="Clear", command=clear, bg='yellow', fg='black', height=4, width=16)
btn3.grid(row=2, column=2, columnspan=2)
btn3.config(font=("Verdana", 15))
btn4 = Button(root, text="Del", command=delete, bg='yellow', fg='black', height=4, width=8)
btn4.grid(row=2, column=4)
btn4.config(font=("Verdana", 15))
btn5 = Button(root, text="7", command=num7, bg='yellow', fg='black', height=4, width=8)
btn5.grid(row=3, column=0)
btn5.config(font=("Verdana", 15))
btn6 = Button(root, text="8", command=num8, bg='yellow', fg='black', height=4, width=8)
btn6.grid(row=3, column=1)
btn6.config(font=("Verdana", 15))
btn7 = Button(root, text="9", command=num9, bg='yellow', fg='black', height=4, width=8)
btn7.grid(row=3, column=2)
btn7.config(font=("Verdana", 15))
btn8 = Button(root, text="+", command=plus, bg='yellow', fg='black', height=4, width=8)
btn8.grid(row=3, column=3)
btn8.config(font=("Verdana", 15))
btn9 = Button(root, text="-", command=minus, bg='yellow', fg='black', height=4, width=8)
btn9.grid(row=3, column=4)
btn9.config(font=("Verdana", 15))
btn10 = Button(root, text="4", command=num4, bg='yellow', fg='black', height=4, width=8)
btn10.grid(row=4, column=0)
btn10.config(font=("Verdana", 15))
btn11 = Button(root, text="5", command=num5, bg='yellow', fg='black', height=4, width=8)
btn11.grid(row=4, column=1)
btn11.config(font=("Verdana", 15))
btn12 = Button(root, text="6", command=num6, bg='yellow', fg='black', height=4, width=8)
btn12.grid(row=4, column=2)
btn12.config(font=("Verdana", 15))
btn13 = Button(root, text="^", command=power, bg='yellow', fg='black', height=4, width=8)
btn13.grid(row=4, column=3)
btn13.config(font=("Verdana", 15))
btn14 = Button(root, text="/", command=div, bg='yellow', fg='black', height=4, width=8)
btn14.grid(row=4, column=4)
btn14.config(font=("Verdana", 15))
btn15 = Button(root, text="1", command=num1, bg='yellow', fg='black', height=4, width=8)
btn15.grid(row=5, column=0)
btn15.config(font=("Verdana", 15))
btn16 = Button(root, text="2", command=num2, bg='yellow', fg='black', height=4, width=8)
btn16.grid(row=5, column=1)
btn16.config(font=("Verdana", 15))
btn17 = Button(root, text="3", command=num3, bg='yellow', fg='black', height=4, width=8)
btn17.grid(row=5, column=2)
btn17.config(font=("Verdana", 15))
btn18 = Button(root, text=".", command=point, bg='yellow', fg='black', height=4, width=8)
btn18.grid(row=6, column=0)
btn18.config(font=("Verdana", 15))
btn19 = Button(root, text="0", command=num0, bg='yellow', fg='black', height=4, width=8)
btn19.grid(row=6, column=1)
btn19.config(font=("Verdana", 15))
btn20 = Button(root, text="*", command=mul, bg='yellow', fg='black', height=4, width=8)
btn20.grid(row=6, column=2)
btn20.config(font=("Verdana", 15))
btn21 = Button(root, text="=", command=solve, bg='yellow', fg='black', height=8, width=16)
btn21.grid(row=5, column=3, rowspan=2, columnspan=2)
btn21.config(font=("Verdana", 15))
root.mainloop()
