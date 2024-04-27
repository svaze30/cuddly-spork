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
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
class blogpost:
    def __init__(self,author,text,srNo):
        self.author=author
        self.text=text
        self.srNo=srNo
        self.comments=[]
        
class comment:
    def __init__(self,author,text):
        self.author=author
        self.text=text