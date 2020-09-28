import PyPDF2

template = PyPDF2.PdfFileReader(open('../static_resources/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('../static_resources/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('../static_resources/watermarked_output.pdf', 'wb') as file:
        output.write(file)
