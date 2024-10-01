from datetime import date
from datetime import time
class Entity:
    def get_att(self):
        s=''
        for v in self.__dict__.values():
            s+=str(v)+'$'
        s=s[:-1]
        s+='#'
        return s
    def sabt(self,filename):
        f=open(filename,'a+')
        att=self.get_att()
        f.write(att)
        f.close()
    def virayesh(self,filename,t):
        old=self.get_att()
        new=''
        for  v in t:
            new+=v+'$'
        new=new[:-1]
        new+='#'
        f=open(filename,'r')
        s=f.read()
        f.close()
        s=s.replace(old, new)
        f=open(filename,'w')
        f.write(s)
        f.close()
    def hazf(self,filename):
        old=self.get_att()
        f=open(filename,'r')
        s=f.read()
        f.close()
        s=s.replace(old, '')
        f=open(filename,'w')
        f.write(s)
        f.close()

class Person(Entity):
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        
        
        
class Student(Person):
    filename='student.txt'
    def __init__(self, name, lastname,age,major,college,phonenumber,score='',certificates=''):
        Person.__init__(self, name, lastname)
        self.age=age
        self.major=major
        self.college=college
        self.phonenumber=phonenumber
        self.score=score
        self.certificates=certificates
    def save(self):
        self.sabt(Student.filename)
    def edit(self,*t):
        self.virayesh(Student.filename,t)
    def delete(self):
        self.hazf(Student.filename)

    def __str__(self):
        return self.name+' '+self.lastname
    @classmethod
    def open_file(cls):
        f=open(Student.filename,'r')
        s=f.read().split('#')
        s.pop()
        lst=[]
        for t in  s:
            v=t.split('$')
            lst.append(Student(v[0], v[1], v[2], v[3], v[4], v[5],v[6],v[7]))
        f.close()
        return lst
    def __str__(self):
        return self.name+' '+self.lastname
    @classmethod
    def read_file(cls):
        f=open(Student.filename,'r')
        s=f.read().split('#')
        s.pop()
        lst=[]
        for t in  s:
            v=t.split('$')
            lst.append(Student(v[0], v[1], v[2], v[3], v[4], v[5],v[6],v[7]))
        f.close()
        return lst
class Interviewer(Person):
    filename='interviewer.txt'
    def __init__(self, name, lastname,expertise):
        Person.__init__(self, name, lastname)
        self.expertise=expertise
    def save(self):
        self.sabt(Interviewer.filename)
    def edit(self,*t):
        self.virayesh(Interviewer.filename,t)
    def delete(self):
        self.hazf(Interviewer.filename)

    def __str__(self):
        return self.name+' '+self.lastname
    @classmethod
    def open_file(cls):
        f=open(Interviewer.filename,'r')
        s=f.read().split('#')
        s.pop()
        lst=[]
        for t in  s:
            v=t.split('$')
            lst.append(Interviewer(v[0], v[1], v[2]))
        f.close()
        return lst
        
        
        
class Interview:
    filename='interview.txt'
    def __init__(self,interview_id,date,student):
        self.student=student
        self.interview_id=interview_id
        self.date=date
        self.time=''
        self.interviewrs=[]
    def set_time(self,time):
        self.time=time
    def __str__(self):
        return self.student.name+' '+self.student.lastname
    def save(self):
        att_student=self.student.get_att()
        att_student=att_student[:-1]
        att=str(self.interview_id)+'%'+str(self.date)+'%'+str(self.time)+'%'+att_student+'%'
        s=''
        for v in self.interviewrs:
            s+=v[0].name+'$'+str(v[0].lastname)+'$'+str(v[0].expertise)+'$'+str(v[1])+'&'
        att+=s
        att+='#'
        
        f=open(Interview.filename,'a+')
        f.write(att)
        f.close()
    @classmethod
    def open_file(cls):
         f=open(Interview.filename,'r')
         s=f.read().split('#')
         lst=[]
         s.pop()  
         for t1 in s:
             v=t1.split('%')
             s=v[2].split('$')
             i=Interview(v[0],v[1], Student(s[0], s[1],s[2],s[3]))
             tf=v[3].split('&')
             tf.pop()
             for t2 in tf:
                 f=t2.split('$')
                 i.add_interviewer(Interviewer(i[0],i[1],i[2]), i[3])
             lst.append(i)
         return lst
    # def get_score(self):
    #         s=0
    #         for v in  self.lst_interview:
    #             s+=v[0].score*v[1]
    #         return s
        

class Score(Entity):
    filename='score.txt'
    def __init__(self,studentname,studentlastname,score):
        self.studentname=studentname
        self.studentlastname=studentlastname
        self.score=score
    def save(self):
        self.sabt(Score.filename)

    def __str__(self):
        return self.name+' '+self.lastname
    @classmethod
    def open_file(cls):
        f=open(Score.filename,'r')
        s=f.read().split('#')
        s.pop()
        lst=[]
        for t in  s:
            v=t.split('$')
            lst.append(Score(v[0], v[1], v[2]))
        f.close()
        return lst
    def __str__(self):
        return self.name+' '+self.lastname
    @classmethod
    def read_file(cls):
        f=open(Score.filename,'r')
        s=f.read().split('#')
        s.pop()
        lst=[]
        for t in  s:
            v=t.split('$')
            lst.append(Score(v[0], v[1], v[2]))
        f.close()
        return lst
