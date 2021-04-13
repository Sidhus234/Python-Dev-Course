import PyPDF2

with open('.\\pdffiles\\dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('.\\pdffiles\\tilt.pdf', 'wb') as new_file:
        writer.write(new_file)



with open('.\\pdffiles\\twopage.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
