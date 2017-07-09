import tkinter
from tkinter.filedialog import askopenfilename
import logViewerProc
import threading

class show_text():
    def __init__(self, txt_object):
        self.txt = txt_object

    def show(self, some_string):
        txt.insert(tkinter.END,some_string)

# функция стартер
def starter():
    change_func = show_text(txt)
    # поток для просмотра файла
    th1 = threading.Thread(target = logViewerProc.open_file, args=(r'{}'.format(path_to_file()),change_func),\
                           daemon = True , name= 'read_file')
    th1.start()

def path_to_file():
    op = askopenfilename()
    return op

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