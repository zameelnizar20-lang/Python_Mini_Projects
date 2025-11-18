
def bmi_calculation(user_input):

    height , weight = map(float,user_input.split(":"))
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    print(bmi)
    
    if bmi < 18:
        print("Under Weight")

    elif 18.5 <= bmi <=24.9:
        print("Normal")
    elif 25 <= bmi <=29:
        print("Over Weight")

    else:
        print("Obses")


bmi_calculation(input("Please Enter the Height and Weight (Height:Weight) :"))