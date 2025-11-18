
operator = ("+" , "-", "*" , "/")
number_1 = int(input("Please enter the 1st number : "))
number_2 = int(input("Please enter the 2nd number : "))
u_operator = input(f"Please select a operator {operator}")

if u_operator == "+":
    value =  number_1 + number_2

elif u_operator == "-":
    value =  number_1 - number_2

elif u_operator == "*":
    value =  number_1 * number_2

elif u_operator == "/":
    value =  number_1 / number_2

else:
    print("Invalid Operation")

print(f"your answer is {value}")
