from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Planner")
root.geometry("800x800")

# Defining the dynamic resize of the grid

def auto_resize(window, nrows, ncolumns):
	for i in range(nrows):
		window.grid_rowconfigure(i, weight=1)
	for i in range(ncolumns):
		window.grid_columnconfigure(i, weight=1)

# Defining the days and hours lists

days = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]

hours = []

for i in range(24):
	hours.append(str(i) + ":00")

# Gridding the external corners

for i in range(len(days)):
	Label(root, text=days[i], relief="groove", fg="white", bg="black", padx=10, pady=10, borderwidth=3).grid(sticky='nswe', row=0, column=1+i)

for i in range(len(hours)):
	Label(root, text=hours[i], relief="groove", fg="white", bg="black", padx=10, pady=10, borderwidth=3).grid(sticky='nswe', row=i+1, column=0)

'''
In order to put many widjets in one row and column use a frame
then grid the frame
'''

# Root's functions call
auto_resize(root, len(hours)+1, len(days)+1)
root.mainloop()
