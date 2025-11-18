import tkinter as tk 


root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

def call():
    content = enter.get()
    label.config(text=f"The Text is {content}")

enter = tk.Entry(root, font=("Arial",30))
enter.pack()

button = tk.Button(root, text="ClickMe" , font=("Arial",20) , command=call)
button.pack()


label = tk.Label(root, text="", font=("Arial",20))
label.pack()

root.mainloop()