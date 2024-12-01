'''from PIL import Image
import pytesseract
print (pytesseract.image_to_string('1.jpg'))
from PIL import Image'''
import pyttsx
'''from tesseract import image_to_string'''
'''import pytesseract
a=(pytesseract.image_to_string('a1.png'))'''


engine = pyttsx.init()
engine.say('hi Noisy image to test Tesseract OCR')
engine.runAndWait()
