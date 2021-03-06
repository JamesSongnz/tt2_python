# Import libraries
import cv2
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
import sys
from pdf2image import convert_from_path
import os

# https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/?ref=rp
# error can not find pdfinfo tool.
# <= need to install pdfinfo tool and add path to env variable of Windows.

'''
# tesseract error
# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
#
# https://github.com/UB-Mannheim/tesseract/wiki

https://www.python2.net/questions-3504.htm


I see steps are scattered in different answers. Based on my recent experience with this pytesseract error on Windows, writing different steps in sequence to make it easier to resolve the error:

1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation.Default installation path at the time the time of this edit was: C:/Users/USER/AppData/Local/Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

4. Set the tesseract path in the script before calling image_to_string:

# pytesseract.pytesseract.tesseract_cmd = r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Tesseract-OCR'#

# Path of the pdf
# PDF_file = "./res/d.pdf"
 
Part #1 : Converting PDF to images 
'''

# Store all the pages of the PDF in a variable
# pages = convert_from_path(PDF_file, 500)

# img = cv2.imread('./imgs/tt_playscr.png.jpg')
# Counter to store images of each page of PDF to image
# image_counter = 1

# Iterate through all the pages stored above
# for page in pages:
    # Declaring filename for each page of PDF as JPG
    # For each page, filename will be:
    # PDF page 1 -> page_1.jpg
    # PDF page 2 -> page_2.jpg
    # PDF page 3 -> page_3.jpg
    # ....
    # PDF page n -> page_n.jpg
    # filename = "page_" + str(image_counter) + ".jpg"
    #
    # # Save the image of the page in system
    # page.save(filename, 'JPEG')
    #
    # # Increment the counter to update filename
    # image_counter = image_counter + 1

''' 
Part #2 - Recognizing text from the images using OCR 
'''
3
# Variable to get count of total number of pages
# filelimit = image_counter - 1

# Creating a text file to write the output
outfile = "out_text.txt"

# Open the file in append mode so that
# All contents of all images are added to the same file
f = open(outfile, "a")

# Iterate from 1 to total number of pages
# for i in range(1, filelimit + 1):
    # Set filename to recognize text from
    # Again, these files will be:
    # page_1.jpg
    # page_2.jpg
    # ....
    # page_n.jpg
    # filename = "page_" + str(i) + ".jpg"

    # Recognize the text as string in image using pytesserct
# text = str(((pytesseract.image_to_string(img))))


filename = 'imgs/tt_playscr.png'
text = str(((pytesseract.image_to_string(Image.open(filename)))))

print(text)
    # The recognized text is stored in variable text
    # Any string processing may be applied on text
    # Here, basic formatting has been done:
    # In many PDFs, at line ending, if a word can't
    # be written fully, a 'hyphen' is added.
    # The rest of the word is written in the next line
    # Eg: This is a sample text this word here GeeksF-
    # orGeeks is half on first line, remaining on next.
    # To remove this, we replace every '-\n' to ''.
# text = text.replace('-\n', '')

    # Finally, write the processed text to the file.
f.write(text)

# Close the file after writing all the text.
f.close()