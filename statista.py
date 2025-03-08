import tkinter as tk
import numpy as np
from tkinter import messagebox
from SGH_Statystyka_wzory.averages import normal_average, value_average, w_average
from SGH_Statystyka_wzory.variances import variance_o1, variance_o2, variance_o3, variance_p,expected
from SGH_Statystyka_wzory.asymetry import normal_asymetry,coe_1,coe_2,coe_3
from SGH_Statystyka_wzory.mediana import median

app = tk.Tk()
app.title('Statista')
def av1():
    a=[float(i) for i in x1.get().split(',')]
    messagebox.showinfo('Średnia', f'Średnia wynosi {normal_average(a)}')
def av2():
    a=[float(i) for i in x1.get().split(',')]
    b=[float(i) for i in x2.get().split(',')]
    messagebox.showinfo('Średnia', f'Średnia wynosi {value_average(list(zip(a,b)))}')
def av3():
    a = [float(i) for i in x1.get().split(',')]
    b = [float(i) for i in x2.get().split(',')]
    messagebox.showinfo('Średnia',f'Średnia wynosi {w_average(list(zip(a,b)))}')
def s1():
    a = [float(i) for i in x1.get().split(',')]
    messagebox.showinfo('Odchylenie standardowe', f'Odchylenie standardowe wynosi {np.sqrt(variance_o1(a))}')
def s2():
    a = [float(i) for i in x1.get().split(',')]
    b = [float(i) for i in x2.get().split(',')]
    messagebox.showinfo('Odchylenie standardowe', f'Odchylenie standardowe wynosi {np.sqrt(variance_o2(list(zip(a, b))))}')
def s3():
    a = [float(i) for i in x1.get().split(',')]
    b = [float(i) for i in x2.get().split(',')]
    messagebox.showinfo('Odchylenie standardowe', f'Odchylenie standardowe wynosi {np.sqrt(variance_o3(list(zip(a, b))))}')
def asymetry():
    a = [float(i) for i in x1.get().split(',')]
    messagebox.showinfo('Asymetria', f'Asymetria wynosi {normal_asymetry(a)}')

def mediana_button():
    a = [float(i) for i in x1.get().split(',')]
    messagebox.showinfo('Mediana', f'Mediana wynosi {median(a)}')

def coe_1_button():
    a=[float(i) for i in x1.get().split(',')]
    messagebox.showinfo('Współczynnik zmienności', f'Współczynnik zmienności wynosi {coe_1(a)}')
def coe_2_button():
    a=[float(i) for i in x1.get().split(',')]
    b=[float(i) for i in x2.get().split(',')]
    messagebox.showinfo('Współczynnik zmienności', f'Współczynnik zmienności wynosi {coe_2(list(zip(a, b)))}')
def coe_3_button():
    a=[float(i) for i in x1.get().split(',')]
    b=[float(i) for i in x2.get().split(',')]
    messagebox.showinfo('Współczynnik zmienności', f'Współczynnik zmienności wynosi {coe_3(list(zip(a, b)))}')

def prob_E():
    a = [float(i) for i in x1.get().split(',')]
    b = [float(i) for i in x2.get().split(',')]
    messagebox.showinfo('Oczekiwana wartość', f'Oczekiwana wartość wynosi {expected(list(zip(a, b)))}')

def prob_Dx():
    a = [float(i) for i in x1.get().split(',')]
    b = [float(i) for i in x2.get().split(',')]
    messagebox.showinfo('Średnie odchylenie', f'Średnie odchylenie wynosi {np.sqrt(variance_p(list(zip(a, b))))}')

txt1 = tk.Label(app, text='Wpisz xi(xj)')
txt1.grid(row=0, column=1)

x1=tk.Entry(app)
x1.grid(row=1,column=1)

txt2 = tk.Label(app, text='Wpisz ni, wi lub p (prawdopodobieństwo)')
txt2.grid(row=2, column=1)

x2=tk.Entry(app)
x2.grid(row=3,column=1)

button_av1=tk.Button(app, text='xj',command=av1)
button_av1.grid(row=4,column=0)

button_av2=tk.Button(app, text='xi*ni',command=av2)
button_av2.grid(row=4,column=1)

button_av3=tk.Button(app, text='xi*wi',command=av3)
button_av3.grid(row=4,column=2)

txt3=tk.Label(app, text='Odchylenie standardowe-(z wariancji obciążonej)')
txt3.grid(row=5,column=1)

button_v1=tk.Button(app, text='xj',command=s1)
button_v1.grid(row=6,column=0)

button_v2=tk.Button(app, text='xi*ni',command=s2)
button_v2.grid(row=6,column=1)

button_v3=tk.Button(app, text='xi*wi',command=s3)
button_v3.grid(row=6,column=2)

txt4=tk.Label(app, text='Asymetria (tylko dla xj)')
txt4.grid(row=7, column=1)

button_as=tk.Button(app, text='asymetria', command=asymetry)
button_as.grid(row=8,column=1)

txt5=tk.Label(app, text='Mediana')
txt5.grid(row=9, column=1)

button_me=tk.Button(app, text='mediana', command=mediana_button)
button_me.grid(row=10,column=1)

txt6=tk.Label(app, text='Współczynnik zmienności')
txt6.grid(row=11,column=1)

button_c1=tk.Button(app, text='xj',command=coe_1_button)
button_c1.grid(row=12,column=0)

button_c2=tk.Button(app, text='xi*ni',command=coe_2_button)
button_c2.grid(row=12,column=1)

button_c3=tk.Button(app, text='xi*wi',command=coe_3_button)
button_c3.grid(row=12,column=2)

txt7=tk.Label(app, text='Prawdopodobieństwo')
txt7.grid(row=13,column=1)

button_p1=tk.Button(app, text='E(x)',command=prob_E)
button_p1.grid(row=14,column=0)

button_p2=tk.Button(app, text='D(x)',command=prob_Dx)
button_p2.grid(row=14,column=1)

#app.configure(bg='cadetblue1')

app.mainloop()
