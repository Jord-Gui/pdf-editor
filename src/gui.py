import tkinter
from tkinter import filedialog

from merge import merge_pdf
from cut import cut_pdf


class PDFEditor:

    def __init__(self, root) -> None:
        root.title("Jord's PDF Editor")
        root.geometry("400x300")

        self.filenames = []

        self.upload_btn = tkinter.Button(root, text='Open', command=self.UploadAction)
        self.upload_btn.pack()

    def UploadAction(self):
        filename = filedialog.askopenfilename()
        if filename:
            print('Selected:', filename)
            self.filenames.append(filename)
        else:
            print('No file selected')


root = tkinter.Tk()
pdfEdit = PDFEditor(root)
root.mainloop()

print(str(pdfEdit.filenames))
