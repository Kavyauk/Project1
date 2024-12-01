

from tkinter import *
from tkinter import filedialog
#import tk.FileDialog as filedialog
#import pyttsx
from PIL import Image,ImageTk
#import pygame
import speech_recognition as sr
import tkinter.filedialog 
from PIL import Image
from tkinter.filedialog import askopenfilename
import pyttsx3
import time
import pytesseract
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email import encoders


root=Tk()
root.title('')
root.geometry('900x800')
root.resizable(width = FALSE ,height= FALSE)
Image_open = Image.open('1.jpg').convert()
image = ImageTk.PhotoImage(Image_open)
logo = Label(root,image=image,bg='Sky Blue')
logo.place(x=0,y=0,bordermode="outside")








def send_mail(status):#'kavyaukkavya@gmail.com', '', 'speech to text', 'This file form python'files = './result/STT.text'
    # Create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # Start TLS for security
    s.starttls()

    # Authentication
    s.login("kavyaukkavya@gmail.com", "qqdj cxnn yigm mdwz")

    # Define message details
    subject = "Test Email with MP3 Attachment"
    message = "Please find the attached MP3 file."

    # Create MIMEMultipart object
    msg = MIMEMultipart()

    # Attach text message
    msg.attach(MIMEText(message, 'plain'))

    if status==1:
        text_file = "./result/STT.txt"
        with open(text_file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(file_data)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
        msg.attach(attachment)
    elif status==2:
    
        # Attach MP3 file
        audio_file = "./result/speech.mp3"
        with open(audio_file, 'rb') as f:
            audio_data = f.read()
        audio = MIMEAudio(audio_data, 'mp3')
        audio.add_header('Content-Disposition', 'attachment', filename=audio_file)
        msg.attach(audio)
    elif status==3:
    
        # Attach MP3 file
        audio_file = "./result/img_speech.mp3"
        with open(audio_file, 'rb') as f:
            audio_data = f.read()
        audio = MIMEAudio(audio_data, 'mp3')
        audio.add_header('Content-Disposition', 'attachment', filename=audio_file)
        msg.attach(audio)
    

    # Set sender, receiver, and subject
    msg['From'] = "kavyaukkavya@gmail.com"
    msg['To'] = "kavyakumar052002@gmail.com"
    msg['Subject'] = subject

    # Convert MIMEMultipart object to string
    text = msg.as_string()

    # Sending the mail
    s.sendmail("kavyaukkavya@gmail.com", "kavyakumar052002@gmail.com", text)

    # Terminating the session
    s.quit()
    print('done')

#*******************************************************************************#
    
def STT():
   
    import speech_recognition as sr
    recording = sr.Recognizer()
    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source)
        print("Please Say something:")
        audio = recording.listen(source)
        print("You said: \n" + recording.recognize_google(audio))
        ad=recording.recognize_google(audio)
        print(type(ad))
        filename = './result/STT.txt'
        f =open(filename,'w')
        f.write(str(ad))
        f.close()
        send_mail(1)
        #try:
            
           # print("You said: \n" + recording.recognize_google(audio))
          #  lcd_init()
    
          #  lcd_string(str(ad),LCD_LINE_1)
            
            #time.sleep(3) 

        #    print(ad)
        #except Exception as e:
          #  print(e)
    
    
#*******************************************************************************#
    

def imgspch():
    t = Tk()
    t.title("Input Screen")
    t.geometry('350x350')
    t.configure(bg='light blue')
    t.resizable(width = FALSE ,height= FALSE)
   
    def browse():
        
        path1=tkinter.filedialog.askopenfilename()
        e2.delete(0, END)
        e2.insert(0, path1)

    e2 = Entry(t,bd=5,text='')
    e2.place(x =50 ,y=150)
    def nw():
        import pyttsx3
        path1 = e2.get()
        global Path1

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        a=(pytesseract.image_to_string(path1))
        print (a)

        engine = pyttsx3.init()
        engine.save_to_file(path1, './result/img_speech.mp3')
        engine.say(a)
        engine.runAndWait()
        send_mail(3)

    browse = Button(t, text='browse',width=5,height=1,relief=RAISED,overrelief=RIDGE,command=browse)
    browse.place(x =250 ,y=100)
    browse = Button(t, text='ok',width=5,height=1,relief=RAISED,overrelief=RIDGE,command=nw)
    browse.place(x =250 ,y=150)
        
    t.mainloop()    

#*******************************************************************************#
    
def CheckLogin():
    t = Tk()
    t.title("Input Screen")
    t.geometry('500x500')
    t.configure(bg='light blue')
    t.resizable(width = FALSE ,height= FALSE)
    e1 = Entry(t,bd=5,text='')
    e1.place(x =50 ,y=50)
    path = e1.get()
    def TTS():
        import pyttsx3
        path = e1.get()
        global Path
        print (path)
        engine = pyttsx3.init()
        engine.say(path)
        engine.save_to_file(path, './result/speech.mp3')
        engine.runAndWait()
        send_mail(2)
        '''global Path
        engine=pyttsx.init()
        engine.say(path)
        engine.runAndwait()'''

    browse = Button(t, text='Input',width=5,height=1,relief=RAISED,overrelief=RIDGE,command=TTS)
    browse.place(x =250 ,y=150)
    
        
    t.mainloop()

#*******************************************************************************#
    


loginbt = Button(root,text = "TextToSpeech",width=20,height=2,bg="Dodger Blue",fg="black",font="5",relief=RAISED,overrelief=RIDGE,command=CheckLogin)
loginbt.place(x =50 ,y=100)
loginbt = Button(root,text = "SpeechToText",width=20,height=2,bg="Dodger Blue",fg="black",font="5",relief=RAISED,overrelief=RIDGE,command=STT)
loginbt.place(x =100 ,y=200)
loginbt = Button(root,text = "image to speech",width=20,height=2,bg="Dodger Blue",fg="black",font="5",relief=RAISED,overrelief=RIDGE,command=imgspch)
loginbt.place(x =250 ,y=100)

root.mainloop()

#*******************************************************************************#



