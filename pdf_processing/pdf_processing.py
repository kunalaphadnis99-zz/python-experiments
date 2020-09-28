import PyPDF2

with open('../static_resources/dummy.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    print(pdf_reader.numPages)
    print(pdf_reader.getPage(0))
