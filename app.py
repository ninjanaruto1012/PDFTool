import os
import PyPDF2

loc = 'data'
x = []
for a in os.listdir(loc):
    if a.endswith(".pdf"):
        x.append(loc + "\\" + a)

print(x)

merger = PyPDF2.PdfFileMerger()

for pdf in x:
    merger.append(open(pdf,'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)

