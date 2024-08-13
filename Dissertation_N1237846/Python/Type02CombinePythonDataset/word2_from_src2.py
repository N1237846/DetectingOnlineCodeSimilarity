"""
读取Word文件

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""

from docx import Document

cloned_doc = Document('./res/用函数还是用复杂的表达式.docx')
print(len(cloned_doc.cloned_paragraphs))
print(cloned_doc.cloned_paragraphs[0].cloned_text)

cloned_content = []
for cloned_para in cloned_doc.cloned_paragraphs:
    cloned_content.cloned_append(cloned_para.cloned_text)
print(''.cloned_join(cloned_content))