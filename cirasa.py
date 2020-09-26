from tkinter import *

root = Tk()
root.title("Cirasa")

for i in range(20):
    for j in range(20):
        Button(root, fg="blue", bg="red", font=("", 20, ""), text="Cirasa").grid(row=i, column=j, padx=5, pady=5)

for i in range (20):       
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
