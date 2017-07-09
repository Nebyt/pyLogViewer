import time


#  file scanning
def tail(f):
    f.seek(0, 2)  # go to the end of the file
    while True:
        line = f.readline()  # read the last line
        if not line:  # if not have any line - wait 1 second
            time.sleep(1)
            continue
        yield line


# open the file what we need
def open_file(path_to_file, write_in_gui):
    f = open(path_to_file, 'r')
    write_in_gui.show(f.read())  # display what in the file we have now
    for line in tail(f):
        write_in_gui.show(line)  # display new line in the file
