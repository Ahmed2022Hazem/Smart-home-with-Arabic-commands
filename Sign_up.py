from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import tkinter as tk

class message ():
    def __init__(self) :
        pass
        
    def showinfo(title,message):
        win=Toplevel()
        win.geometry('300x150')
        win.title(title) 
        Label(win, text=message).place(x=70,y=45)
        Button(win, text='حسناً', command=win.destroy).place(x=120,y=100)

    def showerror(title,error):
        win=Toplevel()
        win.geometry('300x150')
        win.resizable(False,False)
        err= ImageTk.PhotoImage(file=r"path to error photo\err.png")
        label=Label(win,image=err)
        label.image=err
        label.place(x=220,y=30)
        win.title(title) 
        Label(win, text=error).place(x=70,y=45)
        Button(win, text='حسناً', command=win.destroy).place(x=120,y=100)



#Functionality

def clear():
    EmailEntry.delete(0,END)
    UsernameEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    confirmPasswordEntry.delete(0,END)
    check.set(0)

def email_enter(event):
    if EmailEntry.get()=='User @ufe.edu.eg':
        EmailEntry.delete(0,END)

def username_enter(event):
    if UsernameEntry.get()=='Username':
        UsernameEntry.delete(0,END)

def password_enter(event):
    if PasswordEntry.get()=='Password':
        PasswordEntry.delete(0,END)

def confirmPassword_enter(event):
    if confirmPasswordEntry.get()=='confirm Password':
        confirmPasswordEntry.delete(0,END)

def connect_database():
    if(EmailEntry.get()=='' or PasswordEntry.get()==''or UsernameEntry.get()==''or confirmPasswordEntry.get()==''):
        message.showerror('خطأ','يرجى ملأ كل الخانات')
    elif PasswordEntry.get()!=confirmPasswordEntry.get():
        message.showerror('خطأ','كلمة السر غير متطابقة')
    elif check.get()==0:
        message.showerror('خطأ','من فضلك وافق على الشروط و الأحكام')
    else:
        
        try:
          con=pymysql.connect(host='localhost',user='root',password='1Qaz3edc')
          mycursor=con.cursor()
        except:
          message.showerror('خطأ','خطأ فى الاتصال بقاعدة البيانات يرجى اعادة المحاولة')
          return
        try:
           query='create database userdata'
           mycursor.execute(query)
           query='use userdata'
           mycursor.execute(query)
           query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
           mycursor.execute(query)
        except:
            query='use userdata'
            mycursor.execute(query)
        
        query='select * from data where username= %s'
        mycursor.execute(query,(UsernameEntry.get()))
        row=mycursor.fetchone()
        if row!=None:
             message.showerror('خطأ','الاسم موجود بالفعل')
        else:
         query='insert into data(email,username,password) values (%s,%s,%s)'
         mycursor.execute(query,(EmailEntry.get(),UsernameEntry.get(),PasswordEntry.get()))
         message.showinfo('نجاح','تم الاشتراك بنجاح')
         clear()
         con.commit()
         con.close()
        signup_window.destroy()
        import HCILK2

       
    
#GUI

signup_window=tk.Tk()
signup_window.title('انشاء حساب')
signup_window.geometry('879x508+50+50')
signup_window.resizable(FALSE,False)
bgcolor='#ADC8E8'
Textcolor='#000000'
bg=ImageTk.PhotoImage(file=r"path to background photo\bg4.png")



bglabel=Label(signup_window,image=bg)
bglabel.pack()

heading=Label(signup_window,text='حساب انشاء ',font=('Microsoft Yahei UI Light',17,'bold'),bg=bgcolor,fg=Textcolor)
heading.place(x=689,y=55)

email_label=Label(signup_window,text='الالكترونى البريد ',font=('Microsoft Yahei UI Light',10,'bold'),bg=bgcolor,fg=Textcolor)
email_label.place(x=760,y=95)

EmailEntry=Entry(signup_window,bg=Textcolor,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg=bgcolor)
EmailEntry.place(x=637,y=120)
#EmailEntry.insert(0,'User @ufe.edu.eg')
#EmailEntry.bind('<FocusIn>',email_enter)

Username_label=Label(signup_window,text='المستخدم اسم ',font=('Microsoft Yahei UI Light',10,'bold'),bg=bgcolor,fg=Textcolor)
Username_label.place(x=774,y=150)

UsernameEntry=Entry(signup_window,bg=Textcolor,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg=bgcolor)
UsernameEntry.place(x=637,y=175)
#UsernameEntry.insert(0,'Username')
#UsernameEntry.bind('<FocusIn>',username_enter)


password_label=Label(signup_window,text='المرور كلمة ',font=('Microsoft Yahei UI Light',10,'bold'),bg=bgcolor,fg=Textcolor)
password_label.place(x=782,y=205)

PasswordEntry=Entry(signup_window,bg=Textcolor,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg=bgcolor,show='*')
PasswordEntry.place(x=637,y=230)
#PasswordEntry.insert(0,'Password')
#PasswordEntry.bind('<FocusIn>',password_enter)

confirmPassword_label=Label(signup_window,text='المرور كلمة تأكيد ',font=('Microsoft Yahei UI Light',10,'bold'),bg=bgcolor,fg=Textcolor)
confirmPassword_label.place(x=757,y=260)

confirmPasswordEntry=Entry(signup_window,bg=Textcolor,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg=bgcolor,show='*')
confirmPasswordEntry.place(x=637,y=285)
#confirmPasswordEntry.insert(0,'confirm Password')
#confirmPasswordEntry.bind('<FocusIn>',confirmPassword_enter)
check=IntVar()
terms=Checkbutton(signup_window,text=' الأحكام و الشروط على اوافق ',font=('Microsoft Yahei UI Light',9,'bold'),bg=bgcolor,fg=Textcolor,activeforeground=Textcolor,activebackground=bgcolor,cursor='hand2',variable=check)
terms.place(x=689,y=320)

SignupButton=Button(signup_window,text='الاشتراك',font=('Open Sans',16,'bold'),fg=bgcolor,bg=Textcolor,activeforeground=bgcolor,activebackground=Textcolor,cursor='hand2',border=0,width=17,command=connect_database)
SignupButton.place(x=610,y=365)



signup_window.mainloop()