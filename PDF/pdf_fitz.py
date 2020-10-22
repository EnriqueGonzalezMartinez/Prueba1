import fitz

pdf_document = "HORARIOS.pdf"
document = fitz.open(pdf_document)
page = document.loadPage(0)
text = page.getText("text")
print(text)
