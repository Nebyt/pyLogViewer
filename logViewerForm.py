import tkinter,threading
from tkinter.filedialog import *
import time

tm = time.time()

#  постоянное сканирование файла
def tail(f):
    f.seek(0,2) # переходим в конец файла
    while True:
        line = f.readline() # читаем следующую строку
        if not line:  # если строки нет - ждем
            time.sleep(1)
            continue
        yield line

# открываем нужный файл для просмотра
def open_file():
    op = askopenfilename()  # возвращает путь к файлу полностью
    f = open(op,'r')
    txt.insert(END,f.read())
    for line in tail(f):
        txt.insert(END,line)

def call_active():
    txt.pack()
    if time.time() - tm < 1:# кажется это уже не нужно
        root.after(1000,call_active())# кажется это уже не нужно

# поток для просмотра файла
th = threading.Thread(target = open_file, name=1)

# функция стартер
def starter():
    th.start()
    call_active()

# создаем GUI
root = tkinter.Tk()
txt = tkinter.Text(root, width=90, height=30, font="12")
m = tkinter.Menu(root)
root.config(menu=m)
m.add_command(label="Open...",command= starter)
txt.pack()

root.mainloop()