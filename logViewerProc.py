import time
import os

r_file,w_file = os.pipe()
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
def open_file(path_to_file):
    f = open(path_to_file,'r')
    write_to_pipe = os.fdopen(w_file,'w')
    file_before = f.read()
    for file_line in file_before:
        write_to_pipe.write(f.read())
    #logViewerForm.txt.insert(tkinter.END,f.read()) # заменить на то что не будет вызывать импорт
    for line in tail(f):
        write_to_pipe = os.fdopen(w_file, 'w')
        write_to_pipe.write(line)
            # logViewerForm.txt.insert(tkinter.END,line)# заменить на то что не будет вызывать импорт