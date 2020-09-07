from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Orario 1° semestre")
root.geometry('1200x800')

def auto_resize(window, n_row, n_columns):
    for i in range(n_row):
        window.grid_rowconfigure(i, weight=1)
    for i in range(n_columns):
        window.grid_columnconfigure(i, weight=1)

# combobox for teh choice

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
    Button(rem_win, text="Remove", command=blank_cell).grid(row=4, column=0, pady=10)
    Button(rem_win, text="Close window", command=rem_win.destroy).grid(row=5, column=0, pady=10)
    auto_resize(rem_win, 6, 1)

def add():
    new.destroy()
    add_win = Toplevel(root)
    add_win.title("Add cells")
    add_win.geometry("400x200")
    Label(add_win, text="Select the day").pack()
    combo = ttk.Combobox(add_win, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    combo.pack()
    Label(add_win, text="Select the time").pack()
    combo2 = ttk.Combobox(add_win, values=["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"])
    combo2.pack()
    Label(add_win, text="Select the subject").pack()
    combo = ttk.Combobox(add_win, values=["Programmazione", "Elettrotecnica", "Elementi di meccanica teorica ed applicata", "Fisica II"])
    combo.pack()
    Button(add_win, text="Add", command=blank_cell).pack(pady=10)
    Button(add_win, text="Close window", command=add_win.destroy).pack(pady=10)

def blank_cell(i, k):
    # i and k are the coordinate of the inner grid
    Label(root, borderwidth=5, bg="grey", relief="groove").grid(row=i+1, column=k+1, sticky='nswe')

def new_cell(i, k, mat):
    ''' 
    0 --> Programmazione
    1 --> Elettrotecnica
    2 --> Elementi
    3 --> Fisica
    '''
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
    Label(root, borderwidth=5, text=text[mat], bg=color[mat], relief="groove").grid(row=i, column=k+1, sticky='nswe')
    
auto_resize(root, 12, 6)

# Defining edit button

Button(root, bg="black", borderwidth=5, text="EDIT CELLS", fg="white", relief="groove", command=edit).grid(row=0, column=0, sticky='nswe')

# Defining the time column

for i in range(11):
    Label(root, text=str(i+8) + ":00", borderwidth=5, bg="black", fg="white", relief="groove", padx=10, pady=10).grid(sticky='nwse', row=i+1, column=0)

# Defining the day row

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(5):
    Label(root, text=week[i], borderwidth=5, width=20, bg="black", fg="white", relief="groove", padx=10, pady=10).grid(row=0, column=i+1, sticky='nwse')

# Defining the normal cells

for i in range(11):
    for k in range(5):
        Label(root, borderwidth=5, bg="grey", relief="groove").grid(row=i+1, column=k+1, sticky='nswe')

# Defining the checked cells

# PROGRAMMAZIONE
Label(root, borderwidth=5, text="PROGRAMMAZIONE", bg="light blue", relief="groove").grid(row=1, column=1, sticky='nswe')
Label(root, borderwidth=5, text="PROGRAMMAZIONE", bg="light blue", relief="groove").grid(row=2, column=1, sticky='nswe')
Label(root, borderwidth=5, text="PROGRAMMAZIONE", bg="light blue", relief="groove").grid(row=3, column=1, sticky='nswe')
Label(root, borderwidth=5, text="PROGRAMMAZIONE", bg="light blue", relief="groove").grid(row=7, column=2, sticky='nswe')
Label(root, borderwidth=5, text="PROGRAMMAZIONE", bg="light blue", relief="groove").grid(row=8, column=2, sticky='nswe')
Label(root, borderwidth=5, text="PROGRAMMAZIONE", bg="light blue", relief="groove").grid(row=7, column=3, sticky='nswe')
Label(root, borderwidth=5, text="PROGRAMMAZIONE", bg="light blue", relief="groove").grid(row=8, column=3, sticky='nswe')

# ELETTROTECNICA
Label(root, borderwidth=5, text="ELETTROTECNICA\n/PROGRAMMAZIONE", bg="green", relief="groove").grid(row=4, column=1, sticky='nswe')
Label(root, borderwidth=5, text="ELETTROTECNICA", bg="green", relief="groove").grid(row=5, column=1, sticky='nswe')
Label(root, borderwidth=5, text="ELETTROTECNICA", bg="green", relief="groove").grid(row=2, column=2, sticky='nswe')
Label(root, borderwidth=5, text="ELETTROTECNICA", bg="green", relief="groove").grid(row=3, column=2, sticky='nswe')
Label(root, borderwidth=5, text="ELETTROTECNICA", bg="green", relief="groove").grid(row=4, column=4, sticky='nswe')
Label(root, borderwidth=5, text="ELETTROTECNICA", bg="green", relief="groove").grid(row=5, column=4, sticky='nswe')

# ELEMENTI DI MECACNICA TEORICA E APPLICATA 
Label(root, borderwidth=5, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="groove").grid(row=5, column=2, sticky='nswe')
Label(root, borderwidth=5, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="groove").grid(row=6, column=2, sticky='nswe')
Label(root, borderwidth=5, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="groove").grid(row=3, column=3, sticky='nswe')
Label(root, borderwidth=5, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="groove").grid(row=4, column=3, sticky='nswe')
Label(root, borderwidth=5, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="groove").grid(row=5, column=3, sticky='nswe')
Label(root, borderwidth=5, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="groove").grid(row=1, column=4, sticky='nswe')
Label(root, borderwidth=5, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="groove").grid(row=2, column=4, sticky='nswe')

# FISICA 2
Label(root, borderwidth=5, text="FISICA II", bg="orange", relief="groove").grid(row=1, column=3, sticky='nswe')
Label(root, borderwidth=5, text="FISICA II", bg="orange", relief="groove").grid(row=2, column=3, sticky='nswe')
Label(root, borderwidth=5, text="FISICA II", bg="orange", relief="groove").grid(row=1, column=5, sticky='nswe')
Label(root, borderwidth=5, text="FISICA II", bg="orange", relief="groove").grid(row=2, column=5, sticky='nswe')
Label(root, borderwidth=5, text="FISICA II", bg="orange", relief="groove").grid(row=3, column=5, sticky='nswe')

root.mainloop()
