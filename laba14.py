from tkinter import *
import requests
a = Tk()
def a14():
     g = e.get()
     h = i.get()
     if h == "USD":
          k = g * 89,79
         j['text'] = f"{str(k)}"
     if h == "EUR":
         l = g * 97,13
         j['text'] = f"{str(l)}"
a['bg'] = '#fafafa'
a.title('Конвертор')
a.geometry('300x300')
a.resizable(width=False, height=False)
b = Frame(a, bg='#483D8B', bd=5)
b.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
c = Frame(a, bg='#FFC125', bd=5)
c.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
d = Frame(a, bg='#FFC125', bd=5)
d.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
e = Entry(b, bg='#DCDCDC', font=30)
e.pack()
i = Entry(c, bg='#DCDCDC', font=30)
i.pack()
f = Button(b, text='Перевести деньги', command=a14)
f.pack()
j = Label(d, text='У вас: ', bg='#F08080', font=40)
j.pack()
a.mainloop()
