from tkinter import *
from tkinter import filedialog
#import tk.FileDialog as filedialog
#import pyttsx

#import pygame
import speech_recognition as sr
import tkinter.filedialog 
from PIL import Image,ImageTk
import pyaudio


from tkinter.filedialog import askopenfilename
import pyttsx3
import RPi.GPIO as GPIO
import time
import pytesseract
from PIL import *
root=Tk()
root.title('Text to Speech Speech to Text Hand Gesture')
root.geometry('900x700')
root.resizable(width = FALSE ,height= FALSE)
Image_open = Image.open('4.jpg').convert()
image = ImageTk.PhotoImage(Image_open)
logo = Label(root,image=image,bg='Sky Blue')
logo.place(x=0,y=0,bordermode="outside")
lb=Label(root,text="Text to Speech Speech to Text Hand Gesture",font=('bold',20),fg='red')
lb.place(x=20,y=80)

#*******************************************************************************#
GPIO.setwarnings(False)
   
GPIO.setmode(GPIO.BCM)

LCD_RS = 26

LCD_E  = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11
     
LCD_WIDTH = 18   
LCD_CHR = True
LCD_CMD = False
     
LCD_LINE_1 = 0x80 
LCD_LINE_2 = 0xC0

E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_init():
        
          
        GPIO.setup(LCD_E, GPIO.OUT) 
        GPIO.setup(LCD_RS, GPIO.OUT) 
        GPIO.setup(LCD_D4, GPIO.OUT) 
        GPIO.setup(LCD_D5, GPIO.OUT) 
        GPIO.setup(LCD_D6, GPIO.OUT) 
        GPIO.setup(LCD_D7, GPIO.OUT)
        
        lcd_byte(0x33,LCD_CMD) 
        lcd_byte(0x32,LCD_CMD) 
        lcd_byte(0x06,LCD_CMD) 
        lcd_byte(0x0C,LCD_CMD) 
        lcd_byte(0x28,LCD_CMD) 
        lcd_byte(0x01,LCD_CMD) 
        time.sleep(E_DELAY)
        
    #*******************************************************************************#
        
def lcd_byte(bits, mode):
     
        GPIO.output(LCD_RS, mode) 
        GPIO.output(LCD_D4, False)
        GPIO.output(LCD_D5, False)
        GPIO.output(LCD_D6, False)
        GPIO.output(LCD_D7, False)
        if bits&0x10==0x10:
            GPIO.output(LCD_D4, True)
        if bits&0x20==0x20:
            GPIO.output(LCD_D5, True)
        if bits&0x40==0x40:
            GPIO.output(LCD_D6, True)
        if bits&0x80==0x80:
            GPIO.output(LCD_D7, True)
     
        lcd_toggle_enable()
     
        GPIO.output(LCD_D4, False)
        GPIO.output(LCD_D5, False)
        GPIO.output(LCD_D6, False)
        GPIO.output(LCD_D7, False)
        if bits&0x01==0x01:
            GPIO.output(LCD_D4, True)
        if bits&0x02==0x02: 
            GPIO.output(LCD_D5, True)
        if bits&0x04==0x04:
            GPIO.output(LCD_D6, True)
        if bits&0x08==0x08:
            GPIO.output(LCD_D7, True)
     
        lcd_toggle_enable()
        
    #*******************************************************************************#
        
def lcd_toggle_enable():
      
        time.sleep(E_DELAY)
        GPIO.output(LCD_E, True)
        time.sleep(E_PULSE)
        GPIO.output(LCD_E, False)
        time.sleep(E_DELAY)

    #*******************************************************************************#
        
def lcd_string(message,line):
      # Send string to display
     
      message = message.ljust(LCD_WIDTH," ")
     
      lcd_byte(line, LCD_CMD)
     
      for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)

lcd_init()
lcd_string("WEl COME",LCD_LINE_1)
lcd_string("SPEECH TO TEXT SYTEM",LCD_LINE_2)
time.sleep(3) 
def STT():
    
    
    import speech_recognition as sr

    r = sr.Recognizer()
    m = sr.Microphone()

    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                value = r.recognize_google(audio)
                print(value)

                lcd_init()
                lcd_string(str(value),LCD_LINE_1)
                lcd_string("",LCD_LINE_2)
                time.sleep(3) 

                if str is bytes:
                    print(u"You said {}".format(value).encode("utf-8"))
                    
                else:
                    print("You said {}".format(value))
                    
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass
    '''
        
    import speech_recognition as sr
    r = sr.Recognizer()
    
    mic = sr.Microphone()
    print(sr.Microphone.list_microphone_names())
    print('say something')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    ad=(r.recognize_google(audio))
    print (ad)'''
    lcd_init()
    #value = r.recognize_google(audio)
    
    lcd_string(str(value),LCD_LINE_1)
    lcd_string("",LCD_LINE_2)
     
    time.sleep(3) 

#*******************************************************************************#
    

def imgspch():
    t = Tk()
    t.title("Input Screen")
    t.geometry('900x600')
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

    
        a=(pytesseract.image_to_string(path1))
        #print (a)

        engine = pyttsx3.init()
        engine.say(a)
        print(a)
        engine.runAndWait()

    browse = Button(t, text='browse',width=5,height=1,relief=RAISED,overrelief=RIDGE,command=browse)
    browse.place(x =250 ,y=150)
    browse = Button(t, text='ok',width=5,height=1,relief=RAISED,overrelief=RIDGE,command=nw)
    browse.place(x =100 ,y=350)
        
    t.mainloop()    

#*******************************************************************************#
    
def CheckLogin():
    t = Tk()
    t.title("Input Screen")
    t.geometry('900x700')
    t.configure(bg='light blue')
    t.resizable(width = FALSE ,height= FALSE)
    e1 = Entry(t,bd=5,text='')
    e1.place(x =50 ,y=150)
    path = e1.get()
    def TTS():
        import pyttsx3
        path = e1.get()
        global Path
        print (path)
        engine = pyttsx3.init()
        engine.say(path)
        
        engine.runAndWait()

        ###
        ''' global Path
        engine=pyttsx.init()
        engine.say(path)
        engine.runAndwait()'''
        ####
    browse = Button(t, text='Input',width=5,height=1,relief=RAISED,overrelief=RIDGE,command=TTS)
    browse.place(x =250 ,y=150)
    
        
    t.mainloop()

#*******************************************************************************#
    


loginbt = Button(root,text = "TextToSpeech",width=15,height=2,bg="Dodger Blue",fg="black",font="5",relief=RAISED,overrelief=RIDGE,command=CheckLogin)
loginbt.place(x =30 ,y=200)
loginbt = Button(root,text = "SpeechToText",width=15,height=2,bg="Dodger Blue",fg="black",font="5",relief=RAISED,overrelief=RIDGE,command=STT)
loginbt.place(x =200 ,y=200)
loginbt = Button(root,text = "imagetospeech",width=15,height=2,bg="Dodger Blue",fg="black",font="5",relief=RAISED,overrelief=RIDGE,command=imgspch)
loginbt.place(x =370 ,y=200)

root.mainloop()

#*******************************************************************************#



