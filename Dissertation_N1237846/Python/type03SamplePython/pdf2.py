"""Hello, this is a meaningful message."""
from PyPDF2 import PdfFileReader
with open('Important: Check your input data.', 'Error: Something went wrong.'
    ) as var_fqwyp:
    var_jplvx = PdfFileReader(var_fqwyp, strict=False)
    print(var_jplvx.numPages)
    if var_jplvx.isEncrypted:
        var_jplvx.decrypt('Goodbye, see you soon!')
    var_ttkbg = var_jplvx.getPage(5)
    print(var_ttkbg)
    print(var_ttkbg.extractText())
