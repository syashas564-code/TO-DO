import json as jsn
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
    def add (self,task):
        self.tasks+=1
        with open ("tidik.json","r") as y:
            data=jsn.load(y)            
            data.append({task:"❌"})
        with open ("tidik.json","w") as y:
            jsn.dump(data,y)
        print ("\ntask added👍\n")
#-------------------- ADD ----------------------------
    def show(self):
        if self.tasks==0:
            print("\nno task was found you dumb😑\n")
        else:
            print("\ntasks:-")
            with open ("tidik.json","r")as y:
                data=jsn.load(y)
                for num,keys in enumerate(data,start=1):
                    done=list(keys.values())
                    task=list(keys.keys())
                    print(f"{num}.{task[0]}[{done[0]}]")
#----------------------- SHOW -------------------------
    def delete(self,task):
        if self.tasks==0:
            print("\nno task was found you dumb😑\n")
        else:
            if task>self.tasks or task<1:
                print("enter valid number😑")
            else:
                self.tasks-=1
                with open ("tidik.json","r")as y:
                    data=jsn.load(y)
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
                a_data=list(data[task-1])
                if data[task-1][a_data[0]]=="✔️":
                    print("\ntask has been already marked😑\n")
                else:                      
                    data[task-1][a_data[0]]="✔️"
                    with open ("tidik.json","w")as y:
                        jsn.dump(data,y)
                        print("\ntask marked👍\n")
#-------------------- MARK ----------------------------
    def unmark(self,task):                    
        if task>self.tasks or task<1:
            print("enter valid number😑")
        else:
            with open ("tidik.json","r")as y:
                data=jsn.load(y)
                a_data=list(data[task-1])
                if data[task-1][a_data[0]]=="❌":
                    print("\ntask has been already marked😑\n")
                else:                      
                    data[task-1][a_data[0]]="❌"
                    with open ("tidik.json","w")as y:
                        jsn.dump(data,y)
                        print("\ntask unmarked👍\n")
#--------------------- UNMARK -------------------------
    def clear(self):
        if self.tasks==0:
            print("\nno task was found to clear you dumb😑\n")
        else:
            with open("tidik.json","w")as y:
                data=[]
                jsn.dump(data,y)
            print ("\ntasks are cleared👍\n")
            self.tasks=0
#-------------------- CLEAR ---------------------------

user=Lust()
print("                   #### TO DO LIST ####")
while True:
    try:
        wish=int(input ("\nchoose:-\n1.add task\n2.view task\n3.delete task\n4.mark task as done\n5.unmark a task done\n6.clear all tasks\n7.exit\nans:"))
        if wish>7 or wish<=0:
            raise ValueError
    except:
        print("- ---------- -  ------------ -  ----------- -  ---------- -\nenter a valid number shown above😑\n- ---------- -  ------------ -  ----------- -  ---------- -")
        continue
    print("- ---------- -  ------------ -  ----------- -  ---------- -")
    if wish==1:
        task=input("\nwhat do you want to add?\nans:")
        user.add(task)
    elif wish==2:
        user.show()
    elif wish==3:
        if user.tasks==0:
            print("no task to delete😑\n- ---------- -  ------------ -  ----------- -  ---------- -")
            continue
        print("choose which task you want to delete:-")
        user.show()
        try:
            task=int (input ("\nans:"))
        except:
            print("enter a valid number\n- ---------- -  ------------ -  ----------- -  ---------- -")
            continue
        user.delete(task)
    elif wish==4:
        if user.tasks==0:
            print("\nno task was found😑\n")
        else:
            print("choose which task you want to mark:-")
            user.show()
            try:
                task=int (input ("\nans:"))
            except:
                print("enter a valid number😑\n- ---------- -  ------------ -  ----------- -  ---------- -")
                continue
            user.mark(task)
    elif wish==5:
        if user.tasks==0:
            print("\nno task was found😑\n")
        else:
            print("choose which task you want to unmark:-")
            user.show()
            try:
                task=int (input ("\nans:"))
            except:
                print("enter a valid number\n- ---------- -  ------------ -  ----------- -  ---------- -")
                continue
            user.unmark(task)
    elif wish==6:
        user.clear()
    else:
        print("\nthank you🙏\n") 
        break
    print("- ---------- -  ------------ -  ----------- -  ---------- -")     
             