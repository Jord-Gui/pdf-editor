# PDF-Editor
Edit you PDF!!!  
  
References: https://automatetheboringstuff.com/2e/chapter15/

## To do
Add a GUI/Turn it into a web application  
Add parser for command line to do multiple commands at once e.g. merge (cut pdf1) pdf2 

## Installation instructions
Tested working with Python 3.8.5  
Install venv (py -3.8 -m pip install virtualenv)

Windows installation
1. clone repository
2. cd PDF_Editor
3. delete existing pdfenv
4. py -3.8 -m venv pdfenv
5. pdfenv\Scripts\activate
6. pip install PyPDF2
7. cd src

## Usage in terminal
cut_pdf.py pdf_file start end new_pdf_file  
merge_pdf.py new_pdf_file pdf_file_1 pdf_file_2 ... pdf_file_n
