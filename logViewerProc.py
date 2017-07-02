import time,threading
from tkinter.filedialog import *

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
    import logViewerForm
    logViewerForm.txt.insert(END,f.read())
    for line in tail(f):
        logViewerForm.txt.insert(END,line)

# поток для просмотра файла
th = threading.Thread(target = open_file, name=1)