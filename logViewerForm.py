import tkinter
from tkinter.filedialog import askopenfilename
import logViewerProc
import threading
import os
import time


# функция стартер
def starter():
    # поток для просмотра файла
    th1 = threading.Thread(target = logViewerProc.open_file, args=(r'{}'.format(path_to_file()),),daemon = True , name= 'read file')
    th2 = threading.Thread(target = listen_pipe, daemon = True, name= 'listen_pipe')
    th1.start()
    th2.start()

def path_to_file():
    op = askopenfilename()
    return op

def listen_pipe():
    while True:
        read_from_pipe = os.fdopen(logViewerProc.r_file,'r', 1)
        str = read_from_pipe.read()
        if not str:
            continue
        else:
            txt.insert(tkinter.END,str)


# создаем GUI
root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.wm_title("LogViewer")


m = tkinter.Menu(root)
root.config(menu=m)
txt = tkinter.Text(root, width=90, height=30, font="12")
txt.pack()
m.add_command(label="Open...", command=starter)

if __name__ == '__main__':
    root.mainloop()