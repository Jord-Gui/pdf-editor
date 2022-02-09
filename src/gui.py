from cgitb import text
from heapq import merge
from statistics import geometric_mean
import tkinter
from tkinter import filedialog

from merge import merge_pdf
from cut import cut_pdf


class PdfEditor:

    def __init__(self, master, title, geometry) -> None:
        master.title(title)
        master.geometry(geometry)

        self.merge_btn = tkinter.Button(master, text='Merge PDFs', command=lambda: self.merge_files(master, geometry))
        self.merge_btn.pack()

    def open_new_window(self, parent, title, size):
        new_window = tkinter.Toplevel(parent)
        new_window.title(title)
        new_window.geometry(size)
        return new_window

    def select_file(self, window, filenames):
        filename = filedialog.askopenfilename()
        if filename:
            print('Selected: ', filename)
            filenames.append(filename)
            tkinter.Label(window, text=filename).pack()
        else:
            print('No file selected')
        print(filenames)

    def merge_files(self, master, geometry):
        print('Merge selected')
        merge_window = self.open_new_window(master, "Merge PDFs", geometry)

        tkinter.Label(merge_window, text="Select your files in order:").pack()

        filenames = []

        upload_btn = tkinter.Button(merge_window, text='Select File', command=lambda: self.select_file(merge_window, filenames))
        upload_btn.pack()

        merge_btn = tkinter.Button(merge_window, text='Merge Files')
        merge_btn.pack()


root = tkinter.Tk()
pdfEdit = PdfEditor(root, "Jord's PDF Editor", "400x300")
root.mainloop()

