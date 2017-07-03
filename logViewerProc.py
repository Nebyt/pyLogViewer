import time,threading

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
    print(f.read())
    print(f.tell())
    #logViewerForm.txt.insert(END,f.read()) # заменить на то что не будет вызывать импорт
    for line in tail(f):
        print(f.tell())
        #logViewerForm.txt.insert(END,line)# заменить на то что не будет вызывать импорт