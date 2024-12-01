from PIL import Image
import pyttsx3
'''from tesseract import image_to_string'''
import pytesseract
a=(pytesseract.image_to_string('a3.png'))
print (a)

engine = pyttsx3.init()
engine.say(a)
engine.runAndWait()
