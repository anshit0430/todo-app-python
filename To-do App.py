###################################
########TO-DO APP IN PYTHON########
###################################

def task():
    tasks = [] #creating an empty list to add tasks
    print("---WELCOME TO THE TASK MANAGEMENT APPLICATION---")

    total_task = int(input("Enter the no. of tasks you want to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")
    while True:
        operation = int(input("Enter:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/\n"))

        #Adding a Task
        if operation == 1: 
            add = input("Enter the task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...\n")

        #Updating an Existing Task
        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val) #returning the index value of the existing task
                tasks [ind] = up
                print(f"Updated task {up}.\n")

        #Deleting a Task        
        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...\n")

        #Viewing Existing Tasks
        elif operation == 4:
            print(f"Total tasks = {tasks}\n")

        #Exiting the Application
        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input.")

task()