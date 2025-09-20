class Task:
    def __init__(self):
        self.tasks=[]
    def add_task(self):
        task_description=input("Enter task description:")
        self.tasks.append({"description":task_description,"status":"pending"})
        print("task added successfully")
    def view_task(self):
        print("\n---------TO DO LIST-----------")
        for i, task in enumerate(self.tasks,start=1):
            print(f"{i}.{task['description']}-{task['status']}")
    def mark_task(self):
        self.view_task()
        task_no=int(input("enter the task number to mark as completed:"))
        if (1<=task_no<=len(self.tasks)):
            self.tasks[task_no-1]["status"]="completed"
            print(f"Task '{self.tasks[task_no - 1]['description']}' marked as completed.")
        else:
            print("invalid task no")
list1=Task()
while True:
    print("\n========TO DO LIST MANAGER========")
    print("1-add task")
    print("2-view all task")
    print("3-mark task as done")
    print("4-exit")
    choice=input("enter your choice:")
    if choice=='1':
        list1.add_task()
    elif choice=='2':
        list1.view_task()
    elif choice=='3':
        list1.mark_task()
    elif choice=='4':
        print("exited!")
        break
    else:
        print("invalid choice.....pls try again")
        

            



