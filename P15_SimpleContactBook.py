import os 

contact = []



def add_new():
    input_name = input("Please Enter The Name of The User :")
    input_number = input("Please Enter The Number of The User :")
    contact.append({"Name" : input_name , "Number" : input_number})




def View_contact():

    if len(contact) == 0:
        print("No Details to view")

    else:
        for index,names in enumerate(contact,start=1):
            print(f"{index} : {names['Name']} - {names['Number']}")


def Delete_contact():
    
    if len(contact) == 0:
        print("No Details to view")
    
    else:
        del_input =  int(input("Please enter the number that you need to delete : ")) -1
        removed_va = contact.pop(del_input)
        print(removed_va)

def Save():
    with open("Contact_list.txt", "w") as files:
        for i in contact:
            files.write(str(i) + "\n")
    print("Tasks saved successfully (no duplicates)!")




while True:
    print("----- Menu -----")
    print("1.Add a New Contacts")
    print("2.View Contacts")
    print("3.Delete a Contact")
    print("4.Save the Details is a Diffrent File")

    user_input = input("Please Enter the task number that you want to procceed")

    if user_input == "1":
        add_new()
            
    elif user_input == "2":
        View_contact()

    elif user_input == "3":
        Delete_contact()

    elif user_input == "4":
        Save()


        