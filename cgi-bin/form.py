#!/usr/bin/env python

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("""</body>
        </html>""")

import cgi


form = cgi.FieldStorage()
image = form.getfirst("photo", "не задано")

file = open('image.jpg', 'wb')
data = image


file.write(data)




