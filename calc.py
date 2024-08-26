# Простой калькулятор с графическим интерфейсом, созданным c помощью программного пакета Tkinter (программный пакет
# представляет собой интерпретатор, переводящий код приложений с Python на Tcl — высокоуровневый скриптовый язык,который
# используется в быстром прототипировании, создании графических интерфейсов, веб-разработке.)
import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.configure(state='normal')
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)
    answer_entry.configure(state='disabled')


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.configure(bg='#1b1e23')
window.title('Калькулятор')
window.geometry('300x150')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=2, bg='#FFFFFF', fg='#2C3E50', font=('Arial', 10, 'bold'),
                       height=1, command=add)
button_add.place(x=10, y=70)
button_sub = tk.Button(window, text='-', width=2, bg='#FFFFFF', fg='#2C3E50', font=('Arial', 10, 'bold'),
                       height=1, command=sub)
button_sub.place(x=40, y=70)
button_mul = tk.Button(window, text='*', width=2, bg='#FFFFFF', fg='#2C3E50', font=('Arial', 10, 'bold'),
                       height=1, command=mul)
button_mul.place(x=70, y=70)
button_div = tk.Button(window, text='/', bg='#FFFFFF', fg='#2C3E50', font=('Arial', 10, 'bold'), width=2,
                       height=1, command=div)
button_div.place(x=100, y=70)
number1_entry = tk.Entry(window, bg='#FFFFFF', fg='#2C3E50', font=('Arial', 10, 'bold'), width=15)
number1_entry.place(x=180, y=10)
number2_entry = tk.Entry(window, bg='#FFFFFF', fg='#2C3E50', font=('Arial', 10, 'bold'), width=15)
number2_entry.place(x=180, y=40)
answer_entry = tk.Entry(window, bg='#FFFFFF', fg='#2C3E50', font=('Arial', 10, 'bold'), width=26, state='disabled')
answer_entry.place(x=100, y=110)
number1 = tk.Label(window, text='Введите первое число:', bg='#1b1e23', fg='#FFFFFF', font=('Arial', 10, 'bold'))
number1.place(x=10, y=10)
number2 = tk.Label(window, text='Введите второе число:', bg='#1b1e23', fg='#FFFFFF', font=('Arial', 10, 'bold'))
number2.place(x=10, y=40)
answer = tk.Label(window, text='Результат:', bg='#1b1e23', fg='#FFFFFF', font=('Arial', 10, 'bold'))
answer.place(x=10, y=110)

window.mainloop()
