import pdfkit
import os
import re
import markdown

with open("notes.md", "r+", encoding="utf8") as f:
    content = f.read()

html = markdown.markdown(content, extensions=["markdown.extensions.md_in_html"])

with open("in.html","w+", encoding="utf-8") as f:
    with open("style.html", "r+") as g:
        style = g.read()
    f.write(style)
    f.write(html)

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
pdfkit.from_file('in.html', 'out.pdf', configuration=config, options={"enable-local-file-access": "", "dpi": 250})