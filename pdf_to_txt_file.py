from tika import parser

pdf_file = '/Users/kanan/Desktop/2017-2018-az.pdf'
txt_file = 'MyFile2.txt'

raw = parser.from_file(pdf_file)
content_pdf = raw["content"]

content_pdf = content_pdf.splitlines()

for line in content_pdf:
    if len(line) > 0:
        file1 = open(txt_file, "a+")
        file1.writelines(line)
        file1.writelines("\n")
        file1.close()
