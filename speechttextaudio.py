
import speech_recognition as sr
r = sr.Recognizer()
jackhammer = sr.AudioFile('1.wav')
with jackhammer as source:
    audio = r.record(source)
    
print(r.recognize_google(audio))
