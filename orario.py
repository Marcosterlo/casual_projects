from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Orario 1° semestre")
root.geometry('1200x800')

backup=[]

columns = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4
}

rows = {
    "8:00": 0,
    "9:00": 1,
    "10:00": 2,
    "11:00": 3,
    "12:00": 4,
    "13:00": 5,
    "14:00": 6,
    "15:00": 7,
    "16:00": 8,
    "17:00": 9,
    "18:00": 10
}

subject = {
    "Programmazione": 0,
    "Elettrotecnica": 1,
    "Elementi di meccanica teorica ed applicata": 2,
    "Fisica II": 3
}

color = {
    0: "light blue",
    1: "green",
    2: "red",
    3: "orange"
}

text = {
     0: "PROGRAMMAZIONE",
     1: "ELETTROTECNICA",
     2: "ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA",
     3: "FISICA II"
}
 
def auto_resize(window, n_row, n_columns):
    for i in range(n_row):
        window.grid_rowconfigure(i, weight=1)
    for i in range(n_columns):
        window.grid_columnconfigure(i, weight=1)

def read_backup():
    global backup
    with open("/home/marco/operative/casual_projects/backup_uni.txt", "r") as f:
        backup = f.readlines()
    for i in range(11):
        backup[i] = backup[i].rstrip().split(' ')
    for i in range(11):
        for k in range(5):
            if backup[i][k] == 'b':
                Label(root, borderwidth=5, bg="grey", relief="groove").grid(row=i+1, column=k+1, sticky='nswe')
            else:
                Label(root, borderwidth=5, text=text[int(backup[i][k])], bg=color[int(backup[i][k])], relief="groove").grid(row=i+1, column=k+1, sticky='nswe')

def write_backup():
    with open("/home/marco/operative/casual_projects/backup_uni.txt", "w") as f:
        for i in range(11):
            f.write(str(' '.join(str(v) for v in backup[i])) + '\n')

def edit():
    global new
    new = Toplevel(root)
    new.geometry("400x100")
    new.title("Edit cells")
    auto_resize(new, 1, 2)
    new.configure(bg="black")
    Button(new, bg="black", borderwidth=5, text="REMOVE CELLS", fg="white", relief="groove", command=remove).grid(row=0, column=0, sticky='nswe')
    Button(new, bg="black", borderwidth=5, text="ADD CELLS", fg="white", relief="groove", command=add).grid(row=0, column=1, sticky='nswe')

def remove():
    global columns
    global rows
    new.destroy()
    rem_win = Toplevel(root)
    rem_win.title("Remove cells")
    rem_win.geometry("400x200")
    Label(rem_win, text="Select the day").grid(row=0, column=0)
    combo = ttk.Combobox(rem_win, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    combo.grid(row=1, column=0)
    Label(rem_win, text="Select the time").grid(row=2, column=0)
    combo2 = ttk.Combobox(rem_win, values=["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"])
    combo2.grid(row=3, column=0)
    Button(rem_win, text="Remove", command=lambda: blank_cell(rows[combo2.get()], columns[combo.get()])).grid(row=4, column=0, pady=10)
    Button(rem_win, text="Close window", command=rem_win.destroy).grid(row=5, column=0, pady=10)
    auto_resize(rem_win, 6, 1)

def add():
    global columns
    global rows
    global subject
    new.destroy()
    add_win = Toplevel(root)
    add_win.title("Add cells")
    add_win.geometry("400x200")
    Label(add_win, text="Select the day").grid(row=0, column=0)
    combo = ttk.Combobox(add_win, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    combo.grid(row=1, column=0)
    Label(add_win, text="Select the time").grid(row=2, column=0)
    combo2 = ttk.Combobox(add_win, values=["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"])
    combo2.grid(row=3, column=0)
    Label(add_win, text="Select the subject").grid(row=4, column=0)
    combo3 = ttk.Combobox(add_win, values=["Programmazione", "Elettrotecnica", "Elementi di meccanica teorica ed applicata", "Fisica II"])
    combo3.grid(row=5, column=0)
    Button(add_win, text="Add", command=lambda: new_cell(rows[combo2.get()], columns[combo.get()], subject[combo3.get()])).grid(row=6, column=0, pady=10)
    Button(add_win, text="Close window", command=add_win.destroy).grid(row=7, column=0, pady=10)
    auto_resize(add_win, 8, 1)

def blank_cell(i, k):
    global backup
    # i and k are the coordinate of the inner grid
    Label(root, borderwidth=5, bg="grey", relief="groove").grid(row=i+1, column=k+1, sticky='nswe')
    backup[i][k] = 'b'
    write_backup()

def new_cell(i, k, mat):
    global backup
    Label(root, borderwidth=5, text=text[mat], bg=color[mat], relief="groove").grid(row=i+1, column=k+1, sticky='nswe')
    backup[i][k] = mat 
    write_backup()

auto_resize(root, 12, 6)

read_backup()

# Defining edit button

Button(root, bg="black", borderwidth=5, text="EDIT CELLS", fg="white", relief="groove", command=edit).grid(row=0, column=0, sticky='nswe')

# Defining the time column

for i in range(11):
    Label(root, text=str(i+8) + ":00", borderwidth=5, bg="black", fg="white", relief="groove", padx=10, pady=10).grid(sticky='nwse', row=i+1, column=0)

# Defining the day row

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(5):
    Label(root, text=week[i], borderwidth=5, width=20, bg="black", fg="white", relief="groove", padx=10, pady=10).grid(row=0, column=i+1, sticky='nwse')

root.mainloop()
