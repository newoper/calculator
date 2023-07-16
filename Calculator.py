# Импорт библиотеки и создаем окно
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.title('калькулятор')
def calc(key):
    global memory
    if key=="=":
        #Исключаем написание букв
        strl= "-+0123456789.*/" #
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(END,"первый символ не число")
            messagebox.showerror("это не число, хуйло")
            #cсчет
        try:
                result = eval(calc_entry.get())
                calc_entry.insert(END, "=" + str(result))
        except:
                calc_entry.insert(END, "Идиот, это не число!")
                messagebox.showerror("Проверь внимательнее")
            # Чтобы можно было очистить поле
    elif key == "kgz":
            delete = calc_entry.delete(0, END)
    elif key == "<-":
            delete2 = calc_entry.delete(END,0)
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0,END)
        calc_entry.insert(END,key)


# Создаем кнопки
bttn_list = [
    "7","8","9",  "+","-",
    "4","5","6",  "*","/",
    "1","2","3",   "=",
    "0",".","kgz", "<-",
]
r=1
v=0
for i in bttn_list:# С помощью цикла перебираем лист bttn
    rel=""
    cmd=lambda x=i: calc(x) #Возможность нажать на кнопки
    ttk.Button(root,text=i,command=cmd).grid(row=r,column=v)
    v +=1
    if v>4:
        v=0
        r +=1
calc_entry=Entry(root,width=50)#миниокошко,куда вводится
calc_entry.grid(row=0,column=0,columnspan=4)
root.mainloop()
