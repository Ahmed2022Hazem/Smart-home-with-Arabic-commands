import customtkinter as tk
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
from Speaker_recognition import x,Name
import pymysql
from tkinter import messagebox
import tkinter as t2k




def t():
    t=time.time()
    return t
def change_image():
      wav2=ImageTk.PhotoImage(file="path to photo/g.png")
      wav1L.config(image=wav2)
      wav1L.image=wav2

def control(reshaped_text):
    temp1= arabic_reshaper.reshape("افتح النور")
    temp2= arabic_reshaper.reshape("اقفل النور")
    temp3=  arabic_reshaper.reshape("افتح الستاره")
    temp4=  arabic_reshaper.reshape("اقفل الستاره")

    #1,2 led control -- 5,6 motor control
   

    if reshaped_text == temp1:
      ser.write(b'1')
      change_image
    elif reshaped_text == temp2:
      ser.write(b'2')
    elif reshaped_text == temp3:
       ser.write(b'5')
    elif reshaped_text == temp4:
       ser.write(b'6')


def voiceReco():
    recognizer=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        
        recognizer.adjust_for_ambient_noise(mic,duration=0.2)
        audio=recognizer.listen(mic)
        text=recognizer.recognize_google(audio,language='ar-AR')
        reshaped_text=arabic_reshaper.reshape(text)
        bidi_text=get_display(reshaped_text)
        print(reshaped_text)


        try:
          control(reshaped_text)
        except:
           print("bluetooth not connected")
    #textF.delete("1.0","end")
    #textF.insert(END,bidi_text)
    #textF.tag_add("center",1.0,"end")           
    with open(r"path to audio data\s1.wav", "wb") as f:
        f.write(audio.get_wav_data())  
          




def signup_Page():
    root.destroy()
    newroot=t2k.Tk()
    newroot.destroy()
    import Sign_up 

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

try:
       ser = serial.Serial("COM9", 9600, timeout = 1) #Change your port name COM... and your baudrate
except:
      print("bluetooth not connected")


try:
   con=pymysql.connect(host='localhost', user='root',password='1Qaz3edc', database='userdata')
   mycursor=con.cursor()
except:
    messagebox.showerror('Error','Connection is not established Plase Try Again')
    

query='use userdata'
mycursor.execute(query)
query='select * from data where username= %s '
mycursor.execute(query,(Name)) 

row=mycursor.fetchone()
User = None
bgcolor='#ADC8E8'
Textcolor='#F27300'


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
Lighter_color = "#383F52"
medium_color="#E0E0E0"
tk.set_appearance_mode("Light")
tk.set_default_color_theme("blue")
root=tk.CTk()
root.geometry("1000x600")
root.resizable(width=FALSE, height=FALSE)

#rightFrame = Frame(root,background=medium_color,width=600,height=1400,padx=80,pady=40)
mainFrame = Frame(root,background=medium_color,width=2100,height=1300,padx=80,pady=40)
LabelFont=font.Font(size=45)
center=600


notebook = ttk.Notebook(mainFrame,width=2100,height=1140)


control_frame = Frame(notebook,background=medium_color,width=1440,height=1180)
account_frame = Frame(notebook,background=medium_color,width=1440,height=1180)
 
#def control_page():
mic=ImageTk.PhotoImage(file="path to image/mic_1.png")
wav1=ImageTk.PhotoImage(file="path to image/Voice Recognition/ng.png")
wav2=ImageTk.PhotoImage(file="path to image/g.png")

#textF.tag_configure("center",justify='center')
#textF.place(x=540,y=100)
wav1L=Label(control_frame, image=wav1,background=medium_color)
wav1L.place(x=800,y=100)
wav2L=Label(control_frame, image=wav2,background=medium_color)
button=Button(control_frame,command= lambda: voiceReco(),image=mic,background=medium_color, activebackground=medium_color, cursor='hand2',border=0,height=250,width=250,)
button.place(x=910,y=600)
control_frame.pack()

#def account_page():
bt1=ImageTk.PhotoImage(file="path to image/bt1.png")
bt2=ImageTk.PhotoImage(file="path to image/bt2.png")
 
#print(mycursor.execute('select email from data where username =%s',Name))
#lb1=Label(account_frame,text="البريد الالكترونى" ,background=medium_color,font=LabelFont)   
#lb1.place(x=1700,y=500)
#f = open("myfiles.txt", "r")



lab=Label(account_frame,text="",background=medium_color,font=LabelFont)
lab.place(x=50,y=200)
account_frame.pack()



if row == None:
    User="لم يتم التعرف على المستخدم يرجى انشاء حساب جديد  "  
    lb=Label(account_frame,text=User,background=medium_color,font=LabelFont)   
    lb.place(x=1000,y=300)   
    newaccountButton=Button(account_frame,text='انشاء حساب جديد',fg='black',bg=medium_color,font=(20)  ,activeforeground='black',activebackground=medium_color,cursor='hand2',border=0,width=50,height=20, command=signup_Page)
    newaccountButton.place(x=1800,y=700) 
else:
   if (x==1):
      User= "الاسم :اول مستخدم  " # first user
   if (x==2):
      User="الاسم : ثانى مستخدم " # Second user
   if (x==3):
      User="الاسم : ثالث مستخدم"  # Third user
   if (x==4):
      User="الاسم : رابع مستخدم"  # fourth user
   if (x==5):
      User="الاسم : خامس مستخدم " # fifth user  
   lb=Label(account_frame,text=User,background=medium_color,font=LabelFont)   
   lb.place(x=1700,y=300)

   

# Notebook -----------------------------------------------------------------------


notebook.add(account_frame, text="")
notebook.add(control_frame, text="")

notebook.tab(0, image=bt2, compound="left")
notebook.tab(1, image=bt1, compound="left")

style = ttk.Style()
style.theme_create("custom", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [0, 0, 0, 0], "background": medium_color, "borderwidth": 0, "bordercolor": medium_color}},
    "TNotebook.Tab": {"configure": {"padding": [400, 40, 20, 10], "background": medium_color, "foreground": medium_color, "expand": [1, 1, 1, 0], "borderwidth": 0},
                      "map": {"background": [("selected", medium_color)], "foreground": [("selected", medium_color)], "expand": [("selected", [1, 1, 1, 0])]},
                      "focus": {"background": medium_color, "foreground": medium_color}},
})
style.theme_use("custom")
notebook.pack()

#--------------------------------------------------------------------------------------------------------


root.title("المنزل الذكى")
mainFrame.place(x=140,y=40)

root.mainloop()    

