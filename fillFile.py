import time
import sys
import msvcrt
import threading

pressedKey = ''

def press_key():
    global pressedKey
    while True:
        pressedKey = msvcrt.getwch()
        if pressedKey == 'q':
            sys.exit()
        time.sleep(0.5)

th = threading.Thread(target=press_key,name=2)
def fill_file():
    k = 1
    while True:
        if pressedKey == 'q':
            print('Stop the script')
            sys.exit()
        else:
            with open('test.log', 'a') as file:
                file.writelines('Новая строка {} лога\n'.format(k))
            print('Новая строка {} лог\n'.format(k))
            k += 1
        time.sleep(1)

def starter():
    th.start()
    fill_file()

starter()