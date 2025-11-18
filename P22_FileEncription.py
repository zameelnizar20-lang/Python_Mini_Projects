# ----------------------------------------
# 🔐 File Encryption / Decryption Program
# Concepts: ord(), chr(), loops, file I/O
# ----------------------------------------

function = input("Do you whant to Encrypt or Decrypt data ? ('E' / 'D') :").lower()
file_name = input("Please enter the file name that you whant to encript data : ")
number = int(input("Please enter the number EX - 3 :"))


with open(file_name , "r") as file:
    content = file.read()

new_content = ""

if function == "e":

    for ch in content:
        # Encrypt → Add key to ASCII value
        result = chr(ord(ch) + number)
        new_content += result


elif function == "d":

    for ch in content:
        result = chr(ord(ch) - number)
        new_content += result
        

else :
    print("User Enter a Invalid Letter Please Enter ('E or D')")


if function == "e":
    new_file = "Encrypted_output.txt"

elif function == "d":
    new_file = "Decrypted_output.txt"

else:
    print("Invalid choice! Use E or D.")
    exit()


with open (new_file , "w") as n_file:
    n_file.write(new_content)


print(f"✅ Process completed! Output saved in '{new_file}'.")