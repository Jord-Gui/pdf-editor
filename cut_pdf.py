import PyPDF2


pdf_name = input("Enter pdf name: ")
start_page = int(input("Enter starting page number: "))
end_page = int(input("Enter last page number: "))
new_pdf_name = input("Name of new pdf file: ")

pdf_writer = PyPDF2.PdfFileWriter()
pdf_file = open(pdf_name, "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
for pageNum in range(start_page, end_page):
    page_obj = pdf_reader.getPage(pageNum)
    pdf_writer.addPage(page_obj)

pdf_output_file = open(new_pdf_name, "wb")
pdf_writer.write(pdf_output_file)
pdf_output_file.close()