print("Welome to FileMaker. This script will be used for HTML documents.")

# Initialization of the file
file = open('file.html', 'w')

# First writing to file: complete end tags later on
file.write('''
<!DOCTYPE html>
<!--
This document was spawned by FileMaker HTML, version 1.0

Information on FileMaker HTML, version 1.0:
FileMaker HTML, version 1.0, is, as the name suggests, a script that is used to spawn HTML documents. Version 1.0 was the first in development, and therefore its functionality is very limited, currently only towards headers and paragraphs. In later releases of FileMaker HTML, support for other elements (even dynamic ones) will be added, and the user will be able to link up external stylesheets and scripts.
-->
<html>
<head>
<meta charset="UTF-8">
''')

title = input('Please enter the title of the HTML Document: ')
file.write('<title>')
file.write(title)
file.write('</title>')

# HTML document body
file.write('<body>')

headerQuery = input('Would you like to input a header to your document? y/n: ')
while (headerQuery == 'y'):
    header = input('Please enter the title for your header: ')
    file.write('<h1>')
    file.write(header)
    file.write('</h1>')

    paragraphQuery = input('Would you like to input a paragraph for your header? y/n: ')
    while (paragraphQuery == 'y'):
        paragraph = input('Please enter the text for your paragraph: ')
        file.write('<p>')
        file.write(paragraph)
        file.write('</p>')
        paragraphQuery = input('Would you like to append another paragraph? y/n: ')
        if (paragraphQuery == 'y'):
            continue
        else:
            break
        
    headerQuery = input('Would you like to input a header to your document? y/n: ')
    if (headerQuery == 'y'):
        continue
    else:
        break

file.write('''
</body>
</html>
''')

file.close()
