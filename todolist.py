alltasks=[]  #creating empty list for dict of tasks
while True:
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View Pending Tasks")
    print("3. Mark Tasks as Complete")
    print("4. Delete Tasks")
    print("5. View Completed Tasks")
    print("6. Exit")
    choice=int(input("enter your choice (1-6): "))  # 1. Show menu option

    if choice==1:
        task={}
        newtask=input("enter new task: ")
        task['task']=newtask
        task['status']="pending"
        alltasks.append(task)
        print("task added successfully")  #adding tasks
    
    elif choice==2:
        p=[]
        sno=1
        for i in alltasks:
            if i["status"]=="pending":
                p.append(i)
        if not p:
                print("No pending tasks")
        else:
            for i in p:
                if i["status"]=="pending":
                    print("task",sno, ":", i["task"])
                    sno+=1          #view task
    
    elif choice==3:
        ch=1
        
        pending=[]    #creating pending task list
        
        for i in alltasks:
            if i["status"]=="pending":
                pending.append(i)
        if not pending:
                print("No pending tasks")
        else:
                print("your pending tasks are:")
                for i in pending:
                     
                    print(ch, ". ", i["task"])
                    ch+=1
                comp=int(input("which task have u completed?(1/2/3..)"))
                        #asking user which task they have completed

        index=comp-1
        t=pending[index]
        t["status"]="completed"
        for i in alltasks:
             if i['task']==t['task']:
                  i["status"]="completed"
        print("task", comp, "marked as completed successfully")
                            #marking task as complete

    elif choice==4:
        s=1
        print("all tasks are:")
        for i in alltasks:
             print("task", s, ":", i["task"], "; status:", i["status"])
        dlt=int(input("which task you want to delete(1/2/3..)"))
        if 0<dlt<=len(alltasks):
            no=dlt-1
            del alltasks[no]
            print("task deleted successfully")
        else:
            print("invalid number entered")
                                    #deleting task
    
    elif choice==5:
        c=[]
        n=1
        for i in alltasks:
            if i["status"]=="completed":
                c.append(i)
        if not c:
                print("No tasks completed")
        else:
            for i in c:
                print("task",n, ":", i["task"])
                n+=1 
                            #viewing completed tasks

    elif choice==6:
        break