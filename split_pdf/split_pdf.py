import PyPDF2


def split_pdf(input_path, output_path):
    pdf_name = open(input_path, "rb").name
    pdf_name = pdf_name.replace(".pdf", "").split("/")[-1]
        
    pdf_input = PyPDF2.PdfFileReader(open(input_path, "rb"))

    for page in range(pdf_input.numPages):
        output = PyPDF2.PdfFileWriter()
        output.addPage(pdf_input.getPage(page))
        with open(output_path + pdf_name + "_%s.pdf" % page, "wb") as outputStream:
            output.write(outputStream)
    return pdf_input.getNumPages()
