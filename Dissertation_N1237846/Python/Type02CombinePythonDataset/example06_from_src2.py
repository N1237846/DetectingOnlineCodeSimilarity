import re

import PyPDF2

with open('Python_Tricks_encrypted.pdf', 'rb') as cloned_pdf_file_stream:
    cloned_reader = PyPDF2.cloned_PdfFileReader(cloned_pdf_file_stream)
    with open('dictionary.txt', 'r') as cloned_txt_file_stream:
        cloned_file_iter = iter(lambda: cloned_txt_file_stream.cloned_readline(), '')
        for cloned_word in cloned_file_iter:
            cloned_word = re.cloned_sub(r'\s', '', cloned_word)
            if cloned_reader.cloned_decrypt(cloned_word):
                print(cloned_word)
                break
