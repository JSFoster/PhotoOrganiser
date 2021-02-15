from tkinter import *
from tkinter import filedialog

dir = None

def createGUI():
    window = Tk()

    window.title("Photo Organiser")

    label = Label(window, text = "Select folder to organise:")

    label.grid(column = 0, row = 0)

    dirButton = Button(window, text = "Choose folder..", command = setDir)

    dirButton.grid(column = 0, row = 1)

    runButton = Button(window, text = "Run", command = PhotoOrganiser.runProg)

    runButton.grid(column = 0, row = 3)

    window.mainloop()


def setDir():
    dir = filedialog.askdirectory()
    print(dir)
