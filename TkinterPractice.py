import tkinter as tk

root = tk.Tk()
root.title("Display")
root.geometry("500x500")

def chenge_text():
    content = enter.get()
    label_result.config(text=f"{content}")

enter = tk.Entry(root , font=("Arial", 20))
enter.pack(pady=10)

button = tk.Button(root , text="clickMe" , command=chenge_text)
button.pack()


label_result = tk.Label(root, text="", font=("Arial",20))
label_result.pack()

root.mainloop()