import time

def tail(f):
    f.seek(0,2) # переходим в конец файла
    while True:
        line = f.readline() # читаем следующую строку
        if not line:  # если строки нет - ждем
            time.sleep(0.1)
            continue
        yield line

def openLog():
    pathToFile = input('Enter the path to the file: ').strip('"')
    f = open(pathToFile,'r')
    print(f.read(),end = '')
    logStr = tail(f)
    for line in logStr:
        print(line.strip()) # вместо принт вставляем text.insert

openLog()