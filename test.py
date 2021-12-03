import pdfplumber

def plum_daldal(filename):
    with pdfplumber.open(filename) as pdf:
        for i in pdf.pages:
            page = i
            print(i)
            print(page.extract_text())
        print(pdf.pages)
        

plum_daldal("아뱅.pdf")