# pdf-editor
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
2. cd pdf-editor
3. py -3.8 -m venv venv
4. venv\Scripts\activate
6. pip install PyPDF2
7. cd src
8. run commands
9. deactivate

## Usage in terminal
cut.py pdf_file start end new_pdf_file  
merge.py new_pdf_file pdf_file_1 pdf_file_2 ... pdf_file_n
