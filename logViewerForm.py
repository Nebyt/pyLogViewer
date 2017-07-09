import tkinter
from tkinter.filedialog import askopenfilename
import logViewerProc
import threading


# class for show text from file in TEXT field
class ShowText:
    def __init__(self, txt_object):
        self.txt = txt_object

    def show(self, some_string):
        txt.insert(tkinter.END, some_string)
        txt.see(tkinter.END)


# start to watch a file
def starter():
    # send our text field object into class show_text, it is necessary to display the text from opened file
    change_func = ShowText(txt)
    # set the flow to checking file on changes
    th1 = threading.Thread(target=logViewerProc.open_file, args=(r'{}'.format(path_to_file()), change_func),
                           daemon=True, name='read_file')
    # run the flow
    th1.start()

# open the ask open file dialog, return path to file
def path_to_file():
    op = askopenfilename()
    return op


# create GUI
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
