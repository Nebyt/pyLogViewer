import time

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
def open_file(path_to_file, write_in_GUI):
    f = open(path_to_file,'r')
    write_in_GUI.show(f.read())
    for line in tail(f):
        write_in_GUI.show(line)