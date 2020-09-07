from tkinter import *

root = Tk()
root.title("Orario 1° semestre")
root.geometry('1200x800')

def auto_resize(window, n_row, n_columns):
    for i in range(n_row):
        window.grid_rowconfigure(i, weight=1)
    for i in range(n_columns):
        window.grid_columnconfigure(i, weight=1)

auto_resize(root, 12, 6)

# Defining the time column

for i in range(11):
    Label(root, text=str(i+8) + ":00", borderwidth=2, relief="ridge", padx=10, pady=10).grid(sticky='nwse', row=i+1, column=0)

# Defining the day row

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(5):
    Label(root, text=week[i], borderwidth=2, width=20, relief="ridge", padx=10, pady=10).grid(row=0, column=i+1, sticky='nwse')

# Defining the normal cells

for i in range(11):
    for k in range(5):
        Label(root, borderwidth=2, relief="ridge").grid(row=i+1, column=k+1, sticky='nswe')

# Defining the checked cells

# PROGRAMMAZIONE
Label(root, borderwidth=2, text="PROGRAMMAZIONE", bg="light blue", relief="ridge").grid(row=1, column=1, sticky='nswe')
Label(root, borderwidth=2, text="PROGRAMMAZIONE", bg="light blue", relief="ridge").grid(row=2, column=1, sticky='nswe')
Label(root, borderwidth=2, text="PROGRAMMAZIONE", bg="light blue", relief="ridge").grid(row=3, column=1, sticky='nswe')
Label(root, borderwidth=2, text="PROGRAMMAZIONE", bg="light blue", relief="ridge").grid(row=7, column=2, sticky='nswe')
Label(root, borderwidth=2, text="PROGRAMMAZIONE", bg="light blue", relief="ridge").grid(row=8, column=2, sticky='nswe')
Label(root, borderwidth=2, text="PROGRAMMAZIONE", bg="light blue", relief="ridge").grid(row=7, column=3, sticky='nswe')
Label(root, borderwidth=2, text="PROGRAMMAZIONE", bg="light blue", relief="ridge").grid(row=8, column=3, sticky='nswe')

# ELETTROTECNICA
Label(root, borderwidth=2, text="ELETTROTECNICA\n/PROGRAMMAZIONE", bg="green", relief="ridge").grid(row=4, column=1, sticky='nswe')
Label(root, borderwidth=2, text="ELETTROTECNICA", bg="green", relief="ridge").grid(row=5, column=1, sticky='nswe')
Label(root, borderwidth=2, text="ELETTROTECNICA", bg="green", relief="ridge").grid(row=2, column=2, sticky='nswe')
Label(root, borderwidth=2, text="ELETTROTECNICA", bg="green", relief="ridge").grid(row=3, column=2, sticky='nswe')
Label(root, borderwidth=2, text="ELETTROTECNICA", bg="green", relief="ridge").grid(row=4, column=4, sticky='nswe')
Label(root, borderwidth=2, text="ELETTROTECNICA", bg="green", relief="ridge").grid(row=5, column=4, sticky='nswe')

# ELEMENTI DI MECACNICA TEORICA E APPLICATA 
Label(root, borderwidth=2, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="ridge").grid(row=5, column=2, sticky='nswe')
Label(root, borderwidth=2, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="ridge").grid(row=6, column=2, sticky='nswe')
Label(root, borderwidth=2, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="ridge").grid(row=3, column=3, sticky='nswe')
Label(root, borderwidth=2, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="ridge").grid(row=4, column=3, sticky='nswe')
Label(root, borderwidth=2, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="ridge").grid(row=5, column=3, sticky='nswe')
Label(root, borderwidth=2, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="ridge").grid(row=1, column=4, sticky='nswe')
Label(root, borderwidth=2, text="ELEMENTI DI MECCANICA\nTEORICA ED APPLICATA", bg="red", relief="ridge").grid(row=2, column=4, sticky='nswe')

# FISICA 2
Label(root, borderwidth=2, text="FISICA II", bg="orange", relief="ridge").grid(row=1, column=3, sticky='nswe')
Label(root, borderwidth=2, text="FISICA II", bg="orange", relief="ridge").grid(row=2, column=3, sticky='nswe')
Label(root, borderwidth=2, text="FISICA II", bg="orange", relief="ridge").grid(row=1, column=5, sticky='nswe')
Label(root, borderwidth=2, text="FISICA II", bg="orange", relief="ridge").grid(row=2, column=5, sticky='nswe')
Label(root, borderwidth=2, text="FISICA II", bg="orange", relief="ridge").grid(row=3, column=5, sticky='nswe')

root.mainloop()
