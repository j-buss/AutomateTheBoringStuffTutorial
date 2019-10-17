#! /usr/bin/python3

import docx
doc = docx.Document()
doc.add_paragraph("Hello World!")
doc.save("helloworld.docx")
