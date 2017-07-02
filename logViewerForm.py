import tkinter

# функция стартер
def starter():
    from logViewerProc import th
    th.start()

# создаем GUI
root = tkinter.Tk()
m = tkinter.Menu(root)
root.config(menu=m)
m.add_command(label="Open...", command=starter)
txt = tkinter.Text(root, width=90, height=30, font="12")
txt.pack()

if __name__ == '__main__':
    root.mainloop()