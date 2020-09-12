import sys
import PyPDF2


def merge_pdf(new_pdf_name, files):
    '''
    This function merges pdf in order of argument
    '''
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
    return new_pdf_name

if __name__ == "__main__":
    # merge_pdf.py <new pdf file> <pdf file 1> <pdf file 2> ... <pdf file n>
    new_pdf = sys.argv[1]
    files = sys.argv[2:] 
    new_pdf = merge_pdf(new_pdf, files)
