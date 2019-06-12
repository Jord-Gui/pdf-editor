import PyPDF2


number_of_files = int(input("Number of files to merge: "))

files = []
for i in range(number_of_files):
    pdf_file_name = input("Name of pdf file " + str(i + 1) + ": ")
    files.append(pdf_file_name)

new_pdf_name = input("Name of new pdf file: ")

pdf_writer = PyPDF2.PdfFileWriter()
for pdf_name in files:
    pdf_file = open(pdf_name, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for pageNum in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(pageNum)
        pdf_writer.addPage(page_obj)

pdf_output_file = open(new_pdf_name, "wb")
pdf_writer.write(pdf_output_file)
pdf_output_file.close()
