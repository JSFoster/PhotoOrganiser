import os
import exifread
import shutil
from tkinter import *
from tkinter import filedialog
from functools import partial

dir = None
filetype = (".HEIC", ".JPG", ".heic" ".jpg")
months = {1: "01 - January", 2: "02 - February", 3: "03 - March", 4: "04 - April", 5: "05 - May", 6: "06 - June", 7: "07 - July", 8: "08 - August", 9: "09 - September", 10: "10 - October", 11: "11 - November", 12: "12 - December"}

# TODO: Need Hachoir for mov

## DEFINE FUNCTIONS

def createGUI():
    window = Tk()

    window.title("Photo Organiser")

    label = Label(window, text = "Select folder to organise:", width = 20)

    label.grid(column = 0, row = 0, columnspan = 2, padx = 5, pady = 5)

    folderText = Text(window, height = 1, width = 30, state = DISABLED)

    folderText.grid(column = 0, row = 1, columnspan = 2, padx = 5, pady = 5, sticky = E+W)

    dirButton = Button(window, text = "Choose folder..", command = partial(setDir, folderText))

    dirButton.grid(column = 0, row = 2, columnspan = 2, padx = 5, pady = 5)

    runButton = Button(window, text = "Run", command = runProg, width = 10)

    runButton.grid(column = 0, row = 3, padx = 5, pady = 5, sticky = SW)

    flattenButton = Button(window, text = "Flatten", command = flattenProg, width = 10)

    flattenButton.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = SE)

    window.grid_columnconfigure(1, weight = 1)

    window.mainloop()


def setDir(folderText):
    global dir
    dir = filedialog.askdirectory()
    folderText.configure(state = "normal")
    folderText.delete("1.0", END)
    folderText.insert("end", dir)
    folderText.configure(state = "disabled")

def runProg():
    if dir != None:
        print("Running...")
        # for m in months:
        #     if not os.path.exists(dir + "/" + m):
        #         os.makedirs(dir + "/" + m)
        with os.scandir(dir) as entries:
            for entry in entries:
                if entry.name.endswith(filetype):
                    with open(entry, 'rb') as img:
                        tags = exifread.process_file(img)

                        for tag in tags:
                            if tag == 'Image DateTime':
                                date = str(tags[tag]).split(':')
                                year, month = date[0], date[1]
                                if not os.path.exists(dir + "/" + year):
                                    os.makedirs(dir + "/" + year)
                                if not os.path.exists(dir + "/" + year + "/" + months[int(month)]):
                                    os.makedirs(dir + "/" + year + "/" + months[int(month)])
                    shutil.move(dir + "/" + entry.name, dir + "/" + year + "/" + months[int(month)] + "/" + entry.name)

def flattenProg():
    with os.scandir(dir) as entries:
        for entry in entries:
            print(entry)

## START PROGRAM

createGUI()


#
# f = open("IMG_2343.HEIC", 'rb')
#
# tags = exifread.process_file(f)
#
# for tag in tags:
#     if tag == 'Image DateTime':
#         date = str(tags[tag]).split(':')
#         year, month = date[0], date[1]
#         print(year)
#         print(month)
#
