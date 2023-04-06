import PyPDF2

pdfile = ["pdfsample.pdf", "samp.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfile:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')
