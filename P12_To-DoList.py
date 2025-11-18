import os
# Lets make To_Do List
task =[]




def add_new_task():
    user_task = input("Please Enter Your Task Here : ")
    user_dict = {"Task" : user_task , "Status" : "pending"}
    task.append(user_dict)



def view_all_tasks():
    
    if len(task) == 0:
        print("Nothing inside the task list")

    else:
        for index , to_do in enumerate(task,1):
            print(f"{index} {to_do['Task']} : {to_do['Status']} ")



def remove():
    if len(task) == 0:
        print("Nothing inside the task list")

    else:
        for index , to_do in enumerate(task,1):
            print(f"{index} {to_do['Task']} : {to_do['Status']} ")

        print("This is the task list. ")
        remove_task = int(input("what task do you need to remove ('type the numebr') :")) -1
        rem = task.pop(remove_task)
        print(f"You have sucessfully removed {rem} task form the list")

def save_task():
    import os

def save_task():
    if len(task) == 0:
        print("Nothing inside the task list")
    else:
        with open("new_task_list.txt", "w") as file:  # "w" overwrites
            for t in task:
                file.write(str(t) + "\n")
        print("Tasks saved successfully (no duplicates)!")

def exit():
    print("Thank You for comming")






while True:
    print("--- Welcome To The To-Do List ---")
    print("1.Add new tasks")
    print("2.View all tasks")
    print("3.Remove tasks")
    print("4.Save all tasks to a different file")
    print("5.Exit")

    u_input = input("Please Enter the number of task that you want to continue : ")

    # ✅ Check if input is a number
    if not u_input.isdigit():
        print("⚠️ Invalid input! Please enter a number between 1–5.\n")
        continue  # go back to the top of the loop

    u_input = int(u_input)  # safe to convert now

    if u_input == 1:
        add_new_task()

    elif u_input == 2:
        view_all_tasks()

    elif u_input == 3:
        remove()

    elif u_input == 4:
        save_task()

    elif u_input == 5:
        print("Goodbye! 👋")
        break  # exit the loop safely

    else:
        print("⚠️ Invalid number! Please enter between 1–5.\n")


