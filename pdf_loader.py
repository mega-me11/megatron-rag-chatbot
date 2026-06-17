from pypdf import PdfReader  #importing pdf reading tool from library pypdf

def load_pdf(pdf_path):    #pdf path would be passed as an argument through this function
    reader = PdfReader(pdf_path)  #this creates reader object and opens PDF

    text = ""     #container to store all text or data

    for page in reader.pages:
        text += page.extract_text()

    return text