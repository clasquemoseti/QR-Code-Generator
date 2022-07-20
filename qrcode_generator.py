import pyqrcode


link = "https://docs.python.org/3.10/library/re.html?highlight=re#module-re"
qr_code = pyqrcode.create(link)
qr_code.png("re_py_docs.png", scale=5)

qr_code.show()
