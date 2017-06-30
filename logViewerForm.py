import tkinter,threading, time
from tkinter.filedialog import *

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
    txt.insert(END,f.read()) # добавляем содержимое файла в текстовую форму
    for line in tail(f):
        txt.insert(END,line)

# поток для просмотра файла
th = threading.Thread(target = open_file, name=1)

# функция стартер
def starter():
    th.start()

# создаем GUI
root = tkinter.Tk()
txt = tkinter.Text(root, width=90, height=30, font="12")
m = tkinter.Menu(root)
root.config(menu=m)
txt.pack()
m.add_command(label="Open...",command= starter)

root.mainloop()
