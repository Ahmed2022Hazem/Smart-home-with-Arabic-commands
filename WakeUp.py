import customtkinter
from tkinter import *
from tkinter import font
from PIL import ImageTk,Image 
from playsound import playsound
import speech_recognition
import arabic_reshaper
from bidi.algorithm import *
import sys
import serial
from tkinter import ttk
import time

def t():
    t=time.time()
    return t


def WakeUp():
    recognizer=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        
        recognizer.adjust_for_ambient_noise(mic,duration=0.2)
        audio=recognizer.listen(mic)
        text=recognizer.recognize_google(audio,language='ar-AR')
        reshaped_text=arabic_reshaper.reshape(text)
        temp= arabic_reshaper.reshape("كلمة الاستيقاظ wakeup word") 

    with open(r"path to saving audio data\s1.wav", "wb") as f:
        f.write(audio.get_wav_data())  
        if(reshaped_text==temp):
          return 1     




def sleep_mode():
 x=0
 while(x!=1):
      x=WakeUp()
 import Speaker_recognition
 


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')



sleep_mode()   
      
   