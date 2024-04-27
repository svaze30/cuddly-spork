from datetime import *
import datetime

class task:
    def __init__(self,name,deadline):
        self.name=name
        self.deadline=deadline
        self.ID=-1
        if self.deadline>datetime.date.today():
            self.status="PENDING"
        else:
            self.status="OVERDUE"
            
            
class nuser:
    def __init__(self,username,password,profilePic):
        self.username=username
        self.password=password
        self.profilePic=profilePic
        
class blogpost:
    def __init__(self,author,text):
        self.author=author
        self.text=text
        self.comments=[]
        
class comment:
    def __init__(self,author,text):
        self.author=author
        self.text=text