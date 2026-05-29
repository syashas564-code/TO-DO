import json as jsn
from colorama import *
import shutil as stl
init(autoreset=True)
from datetime import datetime,timedelta,date
class Lust():
    def __init__(self):
        try:
            with open("tidik.json","r") as y:
                data=jsn.load(y)
                self.tasks=len(data)
        except FileNotFoundError:
            with open("tidik.json","w") as y:
                data=[]
                jsn.dump(data,y)
                self.tasks=0
#------------------- CORE -----------------------------
    def add (self,task,prio,due):
        self.tasks+=1
        if due=="none":
            adue="none"
        else:
            today=date.today()
            future=timedelta(days=due)
            adue=format(today+future)
        with open ("tidik.json","r") as y:
            if prio=="A":
                prior="HIGH"
            elif prio=="B":
                prior="MID"
            else:
                prior="🥔"
            data=jsn.load(y)            
            data.append({"task":task,"status":"❌","priority":prior,"due":adue})
            s_data=sorted(data,key=lambda x:x["priority"])
        with open ("tidik.json","w") as y:
            jsn.dump(s_data,y)
        print ("\ntask added👍\n")
#-------------------- ADD ----------------------------
    def show(self):
        if self.tasks==0:
            print("\nno task was found you dumb😑\n")
        else:
            print("\ntasks:-")
            with open ("tidik.json","r")as y:
                data=jsn.load(y)
                for num in range(len(data)):
                    if data[num]["due"]=="none":
                        pass
                    else:
                        if date.fromisoformat(data[num]['due'])<date.today():
                            data[num]['due']=Fore.RED+"OVERDUE⚠️" 
                        else:
                            pass
                    print(f"{num+1}.[{data[num]['status']}]{data[num]['task']} | (priority:{data[num]['priority']}) | (due date:{data[num]['due']})")
#----------------------- SHOW -------------------------
    def delete(self,task):
        if task>self.tasks or task<1:
            print(Fore.RED+"enter valid number😑")
        else:
            with open ("tidik.json","r")as y:
                data=jsn.load(y)
                dcsn=input(f"do you really want to delete '{data[task-1]['task']}' from your list?\nans(y/n):")
                if dcsn=="n":
                    print("\nok👍\n")
                else:
                    self.tasks-=1
                    data.pop(task-1)
                    with open ("tidik.json","w")as y:
                        jsn.dump(data,y) 
                    print(f"\ntask deleted👍\n")
#---------------------- DELETE ------------------------
    def mark(self,task):        
        if task>self.tasks or task<1:
            print("enter valid number😑")
        else:
            with open ("tidik.json","r")as y:
                data=jsn.load(y)
                if data[task-1]["status"]=="✔️":
                    print("\ntask has been already marked😑\n")
                else:                      
                    data[task-1]["status"]="✔️"
                    with open ("tidik.json","w")as y:
                        jsn.dump(data,y)
                        print("\ntask marked👍\n")
#-------------------- MARK ----------------------------
    def unmark(self,task):                    
        if task>self.tasks or task<1:
            print("\nenter valid number😑")
        else:
            with open ("tidik.json","r")as y:
                data=jsn.load(y)
                if data[task-1]["status"]=="❌":
                    print("\ntask has been already marked😑\n")
                else:                      
                    data[task-1]["status"]="❌"
                    with open ("tidik.json","w")as y:
                        jsn.dump(data,y)
                        print("\ntask unmarked👍\n")
#--------------------- UNMARK -------------------------
    def clear(self):
            with open("tidik.json","w")as y:
                data=[]
                jsn.dump(data,y)
            print ("\ntasks are cleared👍\n")
            self.tasks=0
#-------------------- CLEAR ---------------------------
    def edit(self,task,ntask):
        with open ("tidik.json","r")as y:
            data=jsn.load(y)
            data[task-1]["task"]=ntask
        with open ("tidik.json","w")as y:
            jsn.dump(data,y)
            print("\nedit successful\n")
#------------------- EDIT TASK ------------------------
    def is_in(self,task):
        with open ("tidik.json","r") as y:
            data=jsn.load(y)
            for num,adata in enumerate (data):
                if task in adata["task"]:
                    return True
                    break
                else:
                    pass
                
user=Lust()
print("                   #### TO DO LIST ####")
while True:
    try:
        wish=int(input ("\nchoose:-\n1.add task\n2.view task\n3.delete task\n4.mark task as done\n5.unmark a task done\n6.clear all tasks\n7.edit task\n8.exit\nans:"))
        if wish>8 or wish<=0:
            raise ValueError
    except:
        print("- ---------- -  ------------ -  ----------- -  ---------- -\nenter a valid number shown above😑\n- ---------- -  ------------ -  ----------- -  ---------- -")
        continue
    print("- ---------- -  ------------ -  ----------- -  ---------- -")
    if wish==1:
        task=input("\nwhat do you want to add?\nans:")
        ii=user.is_in(task)
        if ii==True:
            print("\ntask already exists😑\n- ---------- -  ------------ -  ----------- -  ---------- -\n")
            continue 
        else:
            while True:
                prior=input("\nhow much priority do you give to your task?\nans(A-B-C):")
                if prior not in ("A","B","C"):
                    print("\nERROR:enter priority in upper case and only 'A','B' or 'C'😑\n")
                    continue
                else:
                    break
            ask=input("\ndo you want to add due date\nans(y/n):")
            if ask=="y":
                while True:
                    try:
                        day=int(input("\nhow many days do you have to finish this task\nans:"))
                    except ValueError:
                        print ("\nenter valid day😑\n")
                    user.add(task,prior,day)
                    break
            else:
                user.add(task,prior,"none")
    elif wish==2:
        user.show()
    elif wiish==3:
        if user.tasks==0:
            print("\nno task to delete😑\n- ---------- -  ------------ -  ----------- -  ---------- -")
            continue
        print("\nchoos which task you want to delete:-")
        user.show()
        try:
            task=int (input ("\nans:"))
        except:
            print("\nenter a valid number\n- ---------- -  ------------ -  ----------- -  ---------- -")
            continue
        user.delete(task)
    elif wish==4:
        if user.tasks==0:
            print("\nno task was found😑\n")
        else:
            print("\nchoose which task you want to mark:-")
            user.show()
            try:
                task=int (input ("\nans:"))
            except:
                print("\nenter a valid number😑\n- ---------- -  ------------ -  ----------- -  ---------- -")
                continue
            user.mark(task)
    elif wiish==5:
        if user.tasks==0:
            print("\nno task was found😑\n")
        else:
            print("\nchoose which task you want to unmark:-")
            user.show()
            try:
                task=int (input ("\nans:"))
            except:
                print("\nenter a valid number\n- ---------- -  ------------ -  ----------- -  ---------- -")
                continue
            user.unmark(task)
    elif wiish==6:
        if user.tasks==0:
            print("\nno task was found to clear you dumb😑\n- ---------- -  ------------ -  ----------- -  ----------")
        else:
            dscn=input("\ndo you really want to delete all the task in your list\nans(y/n):")
            if dscn=="n":
                print("\nok👍\n")
                continue 
            user.clear()
    elif wiish==7:
        if user.tasks==0:
            print("\nno task was found😑\n\n- ---------- -  ------------ -  ----------- -  ---------- -")
            continue
        try:
            print ("\nwhich task do you want to edit?\nans:")
            user.show()
            task=int(input("\nchoose:"))
            if task>user.tasks or task<1:
                raise ValueError
        except ValueError:
            print("\nenter a valid number😑\n- ---------- -  ------------ -  ----------- -  ---------- -")
            continue
        ntask=input("\nplease edit:")
        user.edit(task,ntask)
    else:
        print("\nthank you🙏\n") 
        break
    print("- ---------- -  ------------ -  ----------- -  ---------- -")     