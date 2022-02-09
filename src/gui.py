from cgitb import text
from statistics import geometric_mean
import tkinter
from tkinter import filedialog

from merge import merge_pdf
from cut import cut_pdf


class PdfEditor:

    def __init__(self, master, title, geometry) -> None:
        master.title(title)
        master.geometry(geometry)

        self.merge_btn = tkinter.Button(master, text='Merge Files', command=lambda: self.merge_files(master, geometry))
        self.merge_btn.pack()

    def open_new_window(self, parent, title, size):
        new_window = tkinter.Toplevel(parent)
        new_window.title(title)
        new_window.geometry(size)
        return new_window

    def upload_action(self, filenames):
        filename = filedialog.askopenfilenames()
        if filename:
            print('Selected:', filename)
            filenames.append(filename)
        else:
            print('No file selected')
        print(filenames)

    def merge_files(self, master, geometry):
        print('Merge selected')
        merge_window = self.open_new_window(master, "Merge PDFs", geometry)

        filenames = []

        upload_btn = tkinter.Button(merge_window, text='Select Files', command=lambda: self.upload_action(filenames))
        upload_btn.pack()


root = tkinter.Tk()
pdfEdit = PdfEditor(root, "Jord's PDF Editor", "400x300")
root.mainloop()

