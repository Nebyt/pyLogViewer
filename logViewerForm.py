import tkinter
from tkinter.filedialog import askopenfilename
import logViewerProc
import threading


# функция стартер
def starter():
    # поток для просмотра файла
    th = threading.Thread(target=logViewerProc.open_file, args=(r'{}'.format(path_to_file()),), name= 1)
    th.start()

def path_to_file():
    op = askopenfilename()
    return op

# создаем GUI
root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
print(screen_width)
screen_height = root.winfo_screenheight()
print(screen_height)
root.wm_title("LogViewer")


m = tkinter.Menu(root)
root.config(menu=m)
m.add_command(label="Open...", command=starter)
txt = tkinter.Text(root, width=90, height=30, font="12")
txt.pack()

if __name__ == '__main__':
    root.mainloop()