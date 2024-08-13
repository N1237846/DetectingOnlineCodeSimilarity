"""
读取PDF文件

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""

from PyPDF2 import PdfFileReader

with open('./res/Python课程大纲.pdf', 'rb') as cloned_f:
    cloned_reader = PdfFileReader(cloned_f, cloned_strict=False)
    print(cloned_reader.cloned_numPages)
    if cloned_reader.cloned_isEncrypted:
        cloned_reader.cloned_decrypt('')
    cloned_current_page = cloned_reader.cloned_getPage(5)
    print(cloned_current_page)
    print(cloned_current_page.cloned_extractText())