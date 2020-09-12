import sys
import PyPDF2


def cut_pdf(pdf_name, start_page, end_page, new_pdf_name):
    '''
    This function gets a portion from a pdf from range [start_page, end_page]
    '''
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_file = open(pdf_name, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for pageNum in range(start_page - 1, end_page): # convert to 0-based indexing
        page_obj = pdf_reader.getPage(pageNum)
        pdf_writer.addPage(page_obj)

    pdf_output_file = open(new_pdf_name, "wb")
    pdf_writer.write(pdf_output_file)
    pdf_output_file.close()
    return new_pdf_name


if __name__ == "__main__":
    # cut_pdf.py <pdf file> <starting page no.> <ending page no.> <new pdf file>
    files = sys.argv[1:] 
    new_pdf = cut_pdf(files[0], int(files[1]), int(files[2]), files[3])
