import tkinter
from tkinter import filedialog

from merge import merge_pdf
from cut import cut_pdf


def UploadAction():
    filename = filedialog.askopenfilename()
    if filename:
        print('Selected:', filename)
        filenames.append(filename)
    else:
        print('No file selected')


filenames = []

root = tkinter.Tk()
root.title("Jord's PDF Editor")
root.geometry("400x300")

upload_btn = tkinter.Button(root, text='Open', command=UploadAction)
upload_btn.pack()

root.mainloop()

print(str(filenames))