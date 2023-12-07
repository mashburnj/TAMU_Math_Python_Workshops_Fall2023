import numpy as np
import os
from PyPDF2 import PdfWriter, PdfReader

# First, get  the list of submission files.
os.chdir('./submissions/')
SubmissionList = np.array(os.listdir())
SubmissionList = SubmissionList[ np.char.endswith(SubmissionList, '.pdf') ] # filters the list by names ending in ".pdf"
os.chdir('..')

# Then for each, extract the back page and save to a new file in a separate folder.
for submission in SubmissionList:
    inputpdf = PdfReader(open('./submissions/' + submission, "rb"))
    output = PdfWriter()
    output.add_page(inputpdf.pages[-1]) # last page
    with open('./tosharepoint/' + submission, "wb") as outputStream:
        output.write(outputStream)