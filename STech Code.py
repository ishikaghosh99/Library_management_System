from tkinter import *
import os
import smtplib
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import speech_recognition as sr
import pymysql
conn = pymysql.connect("localhost","manali","stech#123","stech")
cur = conn.cursor()
l=[]
l1=[]
l2=[]
l3=[]
# Designing main_screen for login
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("450x300")
 
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Email * ",font=("Arial",12)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",font=("Arial",12)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
   
def speech():
    r=sr.Recognizer()
    print("Speech Recognition")
    with sr.Microphone() as source:
        print("Say Book Name")
        audio=r.listen(source)
        print("Time over")
        try:
            x=r.recognize_google(audio)
            print("Text: "+x.title());  
            title1=x.title()          
        except:
            pass;
        print(title1)
    shows(title1.upper())

def speech1():
    r=sr.Recognizer()
    print("Speech Recognition")
    with sr.Microphone() as source:
        print("Say Book Name")
        audio=r.listen(source)
        print("Time over")
        try:
            x=r.recognize_google(audio)
            print("Text: "+x.title());  
            title1=x.title()          
        except:
            pass;
        print(title1)
    shows1(title1.upper())
def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            if username1=='admin':
                login_screen.destroy()
                fileout1()
            else:
                login_screen.destroy()
                fileout()

        else:
            password_not_recognised()

    else:
        user_not_found()

def insert_book():  
    global root1
    root1 = Toplevel(login_screen2)
    root1.configure(background='light green') 
  
    root1.title("Add Book") 
  
    root1.geometry("450x200") 
    heading =tk.Label(root1, text="Book Id", bg="light green") 
    name = tk.Label(root1, text="Book Title", bg="light green") 

    course = tk.Label(root1, text="Author", bg="light green") 
    genre=tk.Label(root1, text="Genre", bg="light green") 
    sem = tk.Label(root1, text="Copies Available", bg="light green") 
  
    form_no = tk.Label(root1, text="Copies Issued", bg="light green") 
    heading.grid(row=1, column=0) 
    name.grid(row=2, column=0) 
    course.grid(row=3, column=0) 
    genre.grid(row=4,column=0)
    sem.grid(row=5, column=0) 
    form_no.grid(row=6, column=0) 

    global heading_field
    global name_field
    global course_field
    global sem_field
    global form_no_field
    global genre_field
    heading_field=tk.Entry(root1)
    name_field = tk.Entry(root1) 
    course_field = tk.Entry(root1) 
    genre_field=tk.Entry(root1) 
    sem_field = tk.Entry(root1) 
    form_no_field = tk.Entry(root1) 
  
    heading_field.grid(row=1, column=1, ipadx="100")
    name_field.grid(row=2, column=1, ipadx="100") 
    course_field.grid(row=3, column=1, ipadx="100") 
    genre_field.grid(row=4, column=1, ipadx="100") 
    sem_field.grid(row=5, column=1, ipadx="100") 
    form_no_field.grid(row=6, column=1, ipadx="100") 
    space=tk.Label(root1,text="", bg="light green")
    space.grid(row=7,column=1)
    
    submit = tk.Button(root1, text="Submit", fg="Black", bg="grey",command=ins)
    submit.grid(row=8,column=1)
    
def ins():
    bookid=int(heading_field.get())
    title=name_field.get()
    author=course_field.get()
    available=int(sem_field.get())
    issued=int(form_no_field.get())
    genre=genre_field.get()
    if bookid=="" or title=="" or author=="" or available=="" or issued==""or genre=="":
       warning = tk.Label(root1, text="Please enter all the details",bg="light green",fg="red")
       warning.grid(row=9,column=1)
    else:
        sql="insert into BOOK(BOOK_ID,BOOK_TITLE,AUTHOR,GENRE,COPIES_AVAILABLE,COPIES_ISSUED)"\
        "values(%s,%s,%s,%s,%s,%s)"
        val=(bookid,title,author,genre,available,issued)
        cur.execute(sql,val)  
        conn.commit()
        print("book inserted")
        root1.destroy()
    
def delete_book():
    global root2
    root2 = Toplevel(login_screen2)
    root2.configure(background='light green') 
  
    root2.title("Remove Book") 
    root2.geometry("400x120") 
    space=tk.Label(root2,text="", bg="light green")
    id =tk.Label(root2, text="Book Id", bg="light green") 
    space.grid(row=0,column=1)
    id.grid(row=2, column=0) 
    space.grid(row=5,column=1)

    global id_field
    id_field=tk.Entry(root2)
   
    id_field.grid(row=2, column=1, ipadx="100")
   
    submit = tk.Button(root2, text="Submit", fg="Black", bg="grey",command=delt) 
    submit.grid(row=6,column=1) 
    
def delt():
    bookid=id_field.get()
    if bookid=="":
       warning = tk.Label(root2, text="Please enter all the details", bg="light green",fg="red")
       warning.grid(row=8,column=1)
    else:
         cur.execute("delete from BOOK where BOOK_ID=%s",bookid)
         print(" "+bookid+" ")
         print("deleted")
         conn.commit()
         root2.destroy()
    
def fileout1():
    global login_screen2
    login_screen2 = Toplevel(main_screen)
    login_screen2.geometry('2000x2000')
    login_screen2.configure(bg="light blue")
    
    b1= Button(login_screen2,text="Insert", height="2", width="30", command =insert_book)
    b1.pack(side=tk.LEFT, padx=30, pady=0)
    b1.place(x=0,y=0,relx=0.1,rely=0.15,anchor="c")
    b2=Button(login_screen2,text="Delete", height="2", width="30", command =delete_book)
    b2.pack(side=tk.LEFT, padx=30, pady=0)
    b2.place(relx=0.1,rely=0.25,anchor="c")
    b3=Button(login_screen2,text="Search Book", height="2", width="30",command =speech1)
    b3.pack(side=tk.LEFT, padx=30, pady=0)
    b3.place(relx=0.1,rely=0.35,anchor="c")
    
    load = Image.open("library.jfif")
    load=load.resize((1500,840), Image.ANTIALIAS)
    photo =ImageTk.PhotoImage(load)
    panel = Label(login_screen2,image = photo)
    panel.place(x=0,y=0)
    panel.image=photo
    panel.pack(side=tk.RIGHT, padx=30, pady=0)
    panel.place(x=0,y=0,relx=0.67,rely=0.5,anchor="c")
       
    global listBox4
    listBox4=tk.Listbox(login_screen2,height=10,width=30)
    listBox4.pack(side=tk.BOTTOM, padx=30, pady=0)
    listBox4.place(relx=.30, rely=0.75, anchor="c")
    
    global listBox1
    listBox1=tk.Listbox(login_screen2,height=10,width=60)
    listBox1.pack(side=tk.BOTTOM, padx=30, pady=0)
    listBox1.place(relx=.45, rely=0.75, anchor="c")
    
    global listBox2
    listBox2=tk.Listbox(login_screen2,height=10,width=40)
    listBox2.pack(side=tk.BOTTOM, padx=30, pady=0)
    listBox2.place(relx=.6, rely=0.75, anchor="c")
    
    global listBox3
    listBox3=tk.Listbox(login_screen2,height=10,width=30)
    listBox3.pack(side=tk.BOTTOM, padx=30, pady=0)
    listBox3.place(relx=.73, rely=0.75, anchor="c")
    
def fileout():
    login_screen2 = Toplevel(main_screen)
    login_screen2.geometry('2000x2000')
    login_screen2.configure(bg="light blue")
    
    load = Image.open("library.jfif")
    load=load.resize((1500,840), Image.ANTIALIAS)
    photo =ImageTk.PhotoImage(load)
    panel = Label(login_screen2,image = photo)
    panel.place(x=0,y=0)
    panel.image=photo
    panel.pack(side=tk.BOTTOM, padx=30, pady=0)
    panel.place(x=0,y=0,relx=0.67,rely=0.5,anchor="c")
    
    b1=Button(login_screen2,text="Search Book", height="2", width="30", command =speech)
    b1.pack(side=tk.LEFT, padx=30, pady=0)
    b1.place(x=0,y=0,relx=0.1,rely=0.15,anchor="c")
    b2=Button(login_screen2,text="Issue Book", height="2", width="30", command =issue)
    b2.pack(side=tk.LEFT, padx=30, pady=0)
    b2.place(relx=0.1,rely=0.25,anchor="c")

    global listBox
    listBox=tk.Listbox(login_screen2,height=10,width=120)
    listBox.pack(side=tk.BOTTOM, padx=30, pady=0)
    listBox.place(relx=.50, rely=0.75, anchor="c")
    
def shows(bname):
    cur.execute("select BOOK_TITLE from BOOK where GENRE=%s order by COPIES_ISSUED desc",bname)
    res=cur.fetchall()    
    k=0
    for x in res:
        alist=list(res[k])
        l.append(alist)
        k=k+1
    l.sort(key=lambda e: e[0], reverse=True)
    print(l)
    print(type(l))
    for i in range(len(res)):
        listBox.insert(tk.END,l[i])
        
def shows1(bname):
    cur.execute("select BOOK_ID,BOOK_TITLE,AUTHOR,COPIES_AVAILABLE from BOOK where GENRE=%s order by COPIES_ISSUED desc",bname)
    fres=cur.fetchall()
    
    k=0
    for x in fres:
        alist=list(fres[k])
        l.append(alist[0])
        l1.append(alist[1])
        l2.append(alist[2])
        l3.append(alist[3])
        k=k+1
    
    for i in range(len(fres)):
        listBox4.insert(tk.END,l[i])
        listBox1.insert(tk.END,l1[i])
        listBox2.insert(tk.END,l2[i])
        listBox3.insert(tk.END,l3[i])
    
def issue():
    st=""
    b=listBox.curselection()
    if len(b)>0:
        sel=int(listBox.curselection()[0])
        print(sel)
        label=listBox.get(sel)
        print(label[0])
    print("You issued book",label[0])
    TO = username1
    SUBJECT = 'TEST MAIL'
    TEXT = 'The book '+label[0]+" is issued to you successfully."
    # Gmail Sign In
    gmail_sender = 'stechproject1@gmail.com'
    gmail_passwd = 'stech#2020'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    
    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
        st="Book Issued Successfully!!!"
    except:
        print ('error sending mail')
        st="Sorry! Unsuccessful :("
    
    server.quit()
    
    cur.execute("select COPIES_AVAILABLE from BOOK WHERE BOOK_TITLE=%s",label[0])
    a=cur.fetchone()

    cur.execute("select COPIES_ISSUED from BOOK WHERE BOOK_TITLE=%s",label[0])
    b=cur.fetchone()

    a1=int(a[0])-1
    b1=int(b[0])+1
    query="update BOOK set COPIES_AVAILABLE=%s, COPIES_ISSUED=%s where BOOK_TITLE=%s"
    data=(a1,b1,label[0])
    cur.execute(query,data)
    conn.commit()
    last_window(st)
 
def last_window(st):
    new_screen = Tk()
    new_screen.geometry("400x200")
    new_screen.title("Issue Book")
    Label(new_screen,text=st, bg="blue", width="300", height="2", font=("Calibri", 14)).pack()
    
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
    
# Designing Main(first) main_screen
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x400")
    main_screen.title("Account Login")
   
    load = Image.open("login1.jpg")
    load=load.resize((640,480), Image.ANTIALIAS)
    photo =ImageTk.PhotoImage(load)
    panel = Label(main_screen,image = photo)
    panel.place(x=0,y=0)
   
    Label(text="PLEASE CLICK ON LOGIN BUTTON", bg="blue", width="300", height="2", font=("Calibri", 14)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()

    main_screen.mainloop()

main_account_screen()