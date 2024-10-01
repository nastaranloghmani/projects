import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classes import *
from tkinter import PhotoImage
from datetime import date
from datetime import time
item=-1

def create_win(win_title):
    w=Toplevel()
    w.geometry('700x400+300+200')
    w.title(win_title)
    w.configure(bg="#E1F5FE")
    return w
def create_lb_entry(win_name,lb_txt,r,c):
    Label(win_name,text=lb_txt).grid(row=r,column=c)
    ent=Entry(win_name)
    ent.grid(row=r,column=c+1)
    return ent
def create_2button(win_name,txt_button,r,c):
    Button(win_name,text='Back',command=lambda:win_name.destroy()).grid(row=r,column=c)
    bnt=Button(win_name,text=txt_button)
    bnt.grid(row=r,column=c+1)
    return bnt
def create_listbox(classname,win,txt_lb,r,c):
    Label(win,text=txt_lb).grid(row=r,column=c)
    lstobject=classname.open_file()
    lstvar=StringVar(value=lstobject)
    lstbox=Listbox(win,listvariable=lstvar,justify='left')
    lstbox.grid(rowspan=r+4,column=c)
    return lstbox,lstobject
def create_Combobox(class_name,win_name,r,c):
    s=class_name.read_file()
    val=StringVar()
    lst=ttk.Combobox(win_name,textvariable=val,justify='right')
    
    lst['values'] = s
   
    # prevent typing a value
    lst['state'] = 'readonly'
    lst.grid(row=r,column=c)
    return lst,s
win=Tk()
win.geometry('600x500+300+200')
win.title('College Application System')
menubar=Menu()
win.config(menu=menubar)

image_path=PhotoImage(file="/Users/apple/Desktop/d2430351.png")
bg_image=tkinter.Label(win,image=image_path)
bg_image.place(relheight=1,relwidth=1)



studentmenu=Menu(tearoff=0)
applymenu=Menu(tearoff=0)
interviewmenu=Menu(tearoff=0)


def fnewstudent():
    win_add=create_win('New Student Registration')
    entname=create_lb_entry(win_add,'name',0,0)
    entlastname=create_lb_entry(win_add,'last name',0,3)
    entage=create_lb_entry(win_add,'age',2,0)
    entmajor=create_lb_entry(win_add,'major',2,3)
    entcollege=create_lb_entry(win_add,'college',4,0)
    entphonenumber=create_lb_entry(win_add,'phone number',4,3)
    entscore=create_lb_entry(win_add,'score',5,0)
    entcertificates=create_lb_entry(win_add,'certificates',5,3)
    bntadd=create_2button(win_add,'submit',6,0)

    def fadd():
        name=entname.get()
        lastname=entlastname.get()
        age=entage.get()
        major=entmajor.get()
        college=entcollege.get()
        phonenumber=entphonenumber.get()
        score=entscore.get()
        certificates=entcertificates.get()
        s=Student(name,lastname,age,major,college,phonenumber,score,certificates)
        s.save()
        messagebox.showinfo('submit','Thank you!, You have applied for this major!')
        win_add.destroy()

    bntadd.config(command=fadd)

def finterviewer():
    win_add=create_win('Interviewers Registration')
    entname=create_lb_entry(win_add,'name',0,0)
    entlastname=create_lb_entry(win_add,'last name',1,0)
    entexpertise=create_lb_entry(win_add,'expertise',2,0)
    bntadd=create_2button(win_add,'submit',3,0)

    def fadd():
        name=entname.get()
        lastname=entlastname.get()
        expertise=entexpertise.get()
        s=Interviewer(name,lastname,expertise)
        s.save()
        messagebox.showinfo('submit','Interviewer added!')
        win_add.destroy()

    bntadd.config(command=fadd)
def feditstudent():
    win_edit=create_win('Edit students')
    lstbox,lstobject=create_listbox(Student, win_edit,'List of students', 0, 0)
    entnewname=create_lb_entry(win_edit,'name', 1, 1)
    entnewlastname=create_lb_entry(win_edit,'last name', 2, 1)
    entnewage=create_lb_entry(win_edit,'age',3, 1)
    entnewmajor=create_lb_entry(win_edit,'major',4,1)
    entnewcollege=create_lb_entry(win_edit,'college',5,1)
    entnewphonenumber=create_lb_entry(win_edit,'phone number',6,1)
    entnewscore=create_lb_entry(win_edit,'score',7,1)
    entnewcertificates=create_lb_entry(win_edit,'certificates',8,1)
    bntedit=create_2button(win_edit,'Edit', 9, 1)
    def fedit():
        global item
        newname=entnewname.get()
        newlastname=entnewlastname.get()
        newage=entnewage.get()
        newmajor=entnewmajor.get()
        newcollege=entnewcollege.get()
        newphonenumber=entnewphonenumber.get()
        newscore=entnewscore.get()
        newcertificates=entnewcertificates.get()
        lstobject[item].edit(newname,newlastname,newage,newmajor,newcollege,newphonenumber,newscore,newcertificates)
        messagebox.showinfo('Edit','Successfuly edited!')
        win_edit.destroy()
    bntedit.config(command=fedit)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
        entnewname.config(textvariable=nameval)
        entnewlastname.config(textvariable=StringVar(value=lstobject[item].lastname))
        entnewage.config(textvariable=StringVar(value=lstobject[item].age))
        entnewmajor.config(textvariable=StringVar(value=lstobject[item].major))
        entnewcollege.config(textvariable=StringVar(value=lstobject[item].college))
        entnewphonenumber.config(textvariable=StringVar(value=lstobject[item].phonenumber))
        entnewscore.config(textvariable=StringVar(value=lstobject[item].score))
        entnewcertificates.config(textvariable=StringVar(value=lstobject[item].certificates))
    lstbox.bind('<<ListboxSelect>>',fselect)

def fbookinterview():
    s = None
    i = None
    form_interview = create_win('Book Interview')
    
    form_interview.geometry('1200x500+100+100')
    
    Label(form_interview, text='Students', bg='#00E5FF').grid(row=0, column=0)
    list_student, s_students = create_Combobox(Student, form_interview, 1, 0)
    list_interviewer, s_interviewers = create_listbox(Interviewer, form_interview, 'List of Interviewers', 0, 1)
    
    
    Label(form_interview, bg='#00E5FF', text='Student Name').place(x=800, y=45)
    lbname_student = Label(form_interview, bg='#00E5FF', text='###')
    lbname_student.place(x=640, y=45)
    
    Label(form_interview, bg='#00E5FF', text='Student Last Name').place(x=800, y=85)
    lblastname_student = Label(form_interview, bg='#00E5FF', text='###')
    lblastname_student.place(x=640, y=85)

    Label(form_interview, bg='#00E5FF', text='Interviewer Name').place(x=800, y=105)
    lbname_interviewer = Label(form_interview, bg='#00E5FF', text='###')
    lbname_interviewer.place(x=640, y=105)
    

    Label(form_interview, bg='#00E5FF', text='Interview Date and Time').place(x=800, y=125)
    lbdatetime_interview = Label(form_interview, bg='#00E5FF', text='###')
    lbdatetime_interview.place(x=640, y=125)
    
    def ffainal():
        global i
        i.save()  
        messagebox.showinfo('Success Message', 'Final registration completed successfully!')
        form_interview.destroy()
        
    bnt_fanalsave = Button(form_interview, text='Final Registration', command=ffainal)
    bnt_fanalsave.place(x=450, y=445)
    total=IntVar(value=0)
    
    def fadd_interviewer():
        global i,s
        try:
            item = list_student.current()
            i = Interview(1, date.today(), s_students[item])
            lbname_student.configure(text=s_students[item].name)
            lblastname_student.configure(text=s_students[item].lastname)
            lbname_interviewer.configure(text=s_interviewers[0].name)  
            lbdatetime_interview.configure(text=f"{i.date} - {i.time}")
            
            tree.insert('', END, values=(
                s_students[item].name, 
                s_students[item].lastname, 
                s_interviewers[0].name, 
                s_interviewers[0].expertise, 
                i.date, 
                i.time
            ))
        except IndexError:
            messagebox.showerror('Error', 'Student or Interviewer not selected')
            form_interview.attributes('-topmost', 'true')
    
    bntadd_interviewer = Button(form_interview, text='Add', command=fadd_interviewer)
    bntadd_interviewer.grid(row=2, column=0)
    
    columns = ('student_name', 'student_lastname', 'interviewer_name', 'interviewer_expertise', 'interview_date', 'interview_time')
    tree = ttk.Treeview(form_interview, columns=columns, show='headings')
    tree.heading('student_name', text=' Student Name')
    tree.heading('student_lastname', text='Student Last Name')
    tree.heading('interviewer_name', text='Interviewer Name')
    tree.heading('interviewer_expertise', text='Interviewer Expertise')
    tree.heading('interview_date', text='Interview Date')
    tree.heading('interview_time', text='Interview Time')
    tree.grid(row=7, columnspan=5, sticky='nsew')

    def flistboxselect(event):
        global i,s
        item = list_student.current()
        s=s_students[item]
        i=Interview(1, date.today(), s)
        lbname_student.configure(text=s_students[item].name)
        lblastname_student.configure(text=s_students[item].lastname)
        lbname_interviewer.configure(text=s_interviewers[0].name)
        lbdatetime_interview.configure(text=f"{i.date} - {i.time}")

    list_student.bind('<<ComboboxSelected>>', flistboxselect)

def feditinter():
    win_edit=create_win('Edit interviewers')
    lstbox,lstobject=create_listbox(Interviewer, win_edit,'List of interviewers', 0, 0)
    entnewname=create_lb_entry(win_edit,'name', 1, 1)
    entnewlastname=create_lb_entry(win_edit,'last name', 2, 1)
    entnewexpertise=create_lb_entry(win_edit,'expertise',3, 1)
    bntedit=create_2button(win_edit,'Edit', 4, 1)
    def fedit():
        global item
        newname=entnewname.get()
        newlastname=entnewlastname.get()
        newexpertise=entnewexpertise.get()
        lstobject[item].edit(newname,newlastname,newexpertise)
        messagebox.showinfo('Edit','Successfuly edited!')
        win_edit.destroy()
    bntedit.config(command=fedit)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
        entnewname.config(textvariable=nameval)
        entnewlastname.config(textvariable=StringVar(value=lstobject[item].lastname))
        entnewexpertise.config(textvariable=StringVar(value=lstobject[item].expertise))
    lstbox.bind('<<ListboxSelect>>',fselect)

def fscore():
    win_add=create_win('Scores')
    entname=create_lb_entry(win_add,'student name',0,0)
    entlastname=create_lb_entry(win_add,'student last name',1,0)
    entscore=create_lb_entry(win_add,'student score',2,0)
    bntadd=create_2button(win_add,'submit',3,0)

    def fadd():
        name=entname.get()
        lastname=entlastname.get()
        score=entscore.get()
        s=Score(name,lastname,score)
        s.save()
        messagebox.showinfo('submit','Score added!')
        win_add.destroy()

    bntadd.config(command=fadd)


def fapply():
    win_add=create_win('Complete Application')
    lstbox,lstobject=create_listbox(Student, win_add,'List of students', 0, 0)
    entname=create_lb_entry(win_add,'name',1,1)
    entlastname=create_lb_entry(win_add,'last name',2,1)
    entage=create_lb_entry(win_add,'age',3,1)
    entmajor=create_lb_entry(win_add,'major',4,1)
    entcollege=create_lb_entry(win_add,'college',5,1)
    entphonenumber=create_lb_entry(win_add,'phone number',6,1)
    entscore=create_lb_entry(win_add,'score',7,1)
    entcertificates=create_lb_entry(win_add,'certificates',8,1)
    bntadd=create_2button(win_add,'apply',9,1)

    def fadd():
        global item
        name=entname.get()
        lastname=entlastname.get()
        age=entage.get()
        major=entmajor.get()
        college=entcollege.get()
        phonenumber=entphonenumber.get()
        score=entscore.get()
        certificates=entcertificates.get()
        # s=Student(name,lastname,age,major,college,phonenumber,score,certificates)
        # s.save()
        lstobject[item].edit(name,lastname,age,major,college,phonenumber,score,certificates)
        messagebox.showinfo('apply','Congrats!, Your appliction completed!')
        win_add.destroy()

    bntadd.config(command=fadd)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
        entname.config(textvariable=nameval)
        entlastname.config(textvariable=StringVar(value=lstobject[item].lastname))
        entage.config(textvariable=StringVar(value=lstobject[item].age))
        entmajor.config(textvariable=StringVar(value=lstobject[item].major))
        entcollege.config(textvariable=StringVar(value=lstobject[item].college))
        entphonenumber.config(textvariable=StringVar(value=lstobject[item].phonenumber))
        entscore.config(textvariable=StringVar(value=lstobject[item].score))
        entcertificates.config(textvariable=StringVar(value=lstobject[item].certificates))
    lstbox.bind('<<ListboxSelect>>',fselect)
def freject():
    win_delete=create_win('Reject students')
    lstbox,lstobject=create_listbox(Student, win_delete,'List of students', 0, 0)
    # entname=create_lb_entry(win_delete,'name', 1, 1)
    # entlastname=create_lb_entry(win_delete,'last name', 2, 1)
    # entage=create_lb_entry(win_delete,'age',3, 1)
    # entmajor=create_lb_entry(win_delete,'major',4,1)
    # entcollege=create_lb_entry(win_delete,'college',5,1)
    # entphonenumber=create_lb_entry(win_delete,'phone number',6,1)
    bntedit=create_2button(win_delete,'Reject', 8, 1)
    def fdelete():
        global item
        # name=entname.get()
        # lastname=entlastname.get()
        # age=entage.get()
        # major=entmajor.get()
        # college=entcollege.get()
        # phonenumber=entphonenumber.get()
        lstobject[item].delete()
        messagebox.showinfo('Reject','Student rejected!')
        win_delete.destroy()
    bntedit.config(command=fdelete)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
        # entname.config(textvariable=nameval)
        # entlastname.config(textvariable=StringVar(value=lstobject[item].lastname))
        # entage.config(textvariable=StringVar(value=lstobject[item].age))
        # entmajor.config(textvariable=StringVar(value=lstobject[item].major))
        # entcollege.config(textvariable=StringVar(value=lstobject[item].college))
        # entphonenumber.config(textvariable=StringVar(value=lstobject[item].phonenumber))
    lstbox.bind('<<ListboxSelect>>',fselect)


def fdeleteinter():
    win_delete=create_win('Delete interviewers')
    lstbox,lstobject=create_listbox(Interviewer, win_delete,'List of interviewers', 0, 0)
    bntedit=create_2button(win_delete,'Delete', 8, 1)

    def fdelete():
        global item
        lstobject[item].delete()
        messagebox.showinfo('Delete','Interviewer deleted!')
        win_delete.destroy()
    bntedit.config(command=fdelete)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
    lstbox.bind('<<ListboxSelect>>',fselect)

studentmenu.add_command(label='New Student Registration',command=fnewstudent)
studentmenu.add_command(label='Interviewers Registration',command=finterviewer)
studentmenu.add_command(label='Edit students',command=feditstudent)
studentmenu.add_command(label='Reject Student',command=freject)
studentmenu.add_command(label='Edit Interviewers',command=feditinter)
studentmenu.add_command(label='Delete interviewers',command=fdeleteinter)


interviewmenu.add_command(label='Book an Interview',command=fbookinterview)
interviewmenu.add_command(label='Scores',command=fscore)


applymenu.add_command(label='Complete Application',command=fapply)

menubar.add_cascade(label='Register',menu=studentmenu)
menubar.add_cascade(label='Interview',menu=interviewmenu)
menubar.add_cascade(label='Apply',menu=applymenu)


win.mainloop()


