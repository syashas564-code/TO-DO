class Lust():
    def __init__(self):
        try:
            with open("to do list.txt","r") as y:
                self.tasks=len(y.readlines())
        except FileNotFoundError:
                with open("to do list.txt","w"):
                    pass
                self.tasks=0
#------------- ADD --------------
    def add(self,task):
        
        with open("to do list.txt","a") as y:
            if self.tasks==0:
                y.write(task)
            else:
                y.write("\n"+task)
            print("\ntask added👍\n")
            self.tasks+=1
            
#------------- SHOW -------------
    def show(self):
        if self.tasks==0:
            print("\nNo task was found😑")
        else:
            with open("to do list.txt","r") as y:
                a=y.readlines()
                print("\ntasks:-")
                for num,value in enumerate (a,start=1):
                    print(f"{num}.{value}",end="")
                print()
#----------- DELETE ------------
    def delete(self,task):
        if self.tasks==0:
            print("\nnothing inside to delete😑")
        else:     
            if task>self.tasks or task<0:
                print("\nenter valid number😑\n")
            else:
                self.tasks-=1
                with open("to do list.txt","r") as y:
                    a=y.readlines()
                    a.pop(task-1)
                with open ("to do list.txt","w") as y:
                    y.writelines(a)
                    print ("\ntask deleted\n")
#----------- MARK --------------
    def mark (self,task):
        if self.tasks==0:
            print("\nnothing inside to mark 😑")
        else:     
            if task>self.tasks or task<0:
                print("\nenter valid number😑\n")
            else:
                with open ("to do list.txt","r") as y:
                    a=y.readlines()
                    a[task-1] = a[task-1].rstrip("\n") + "✅\n"
                    
                with open ("to do list.txt","w") as y:
                    y.writelines(a)
                    print("\nmarked\n")
#----------- UN MARK -----------
    def unmark(self,task):
        if self.tasks==0:
            print("\nnothing inside to unmark 😑")
        else:     
            if task>self.tasks or task<0:
                print("\nenter valid number😑\n")
            else:
                with open ("to do list.txt","r") as y:
                    a=y.readlines()
                    a[task-1] = a[task-1].replace("✅", "").rstrip("\n") + "\n"
                with open ("to do list.txt","w") as y:
                    y.writelines(a)
                    print ("\nunmarked👍\n")
#----------- CLEAR -------------
    def clear(self):
        with open("to do list.txt","w") as y:
            print("\ncleared\n")   
            self.tasks-=self.tasks   
#----------- MAIN PROGRAM ---------                 

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
        print("choose which task you want to mark:-")
        user.show()
        try:
            task=int (input ("\nans:"))
        except:
            print("enter a valid number\n- ---------- -  ------------ -  ----------- -  ---------- -")
            continue
        user.mark(task)
    elif wish==5:
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
                                          